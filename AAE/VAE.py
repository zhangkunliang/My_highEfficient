import torch
from torch import nn
from torch import optim
import numpy as np
import torch.nn.functional as F
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import os
import time

start_time = time.time()
LR = 1e-3  # learning rate
num_epochs = 100
BATCH_SIZE = 10

dataPath = r'F:\dataSet\disorder\disorderDataSets\dataSets'


# 数据增强方法抖动
def jittering(array):
    noise = np.random.normal(0, 0.03, array.shape)
    jittered = noise + array
    return jittered


# 数据增强方法缩放
def scaling(array):
    noise = np.random.normal(1, 0.1, array.shape)
    scaled = noise * array
    return scaled


def getDataTensor(iter):
    list_feature = []
    list_th = []
    for inner in os.listdir(dataPath):
        featurePath = os.path.join(dataPath, inner, 'feature.data')
        with open(featurePath, 'r') as fi:
            array = [[float(j) for j in i.strip().split(' ')] for i in fi.readlines()]
            list_feature.append(array)
            array = np.array(array)
            for i in range(iter):
                jitterd = jittering(array)
                list_feature.append(jitterd.tolist())
                scaled = scaling(array)
                list_feature.append(scaled.tolist())
        fi.close()
        thPath = os.path.join(dataPath, inner, 'Thermal_conductivity.txt')
        with open(thPath, 'r') as f:
            th = [float(i) for i in f.readlines()]
            list_th.append(th)
            for i in range(2 * iter):
                list_th.append(th)
        f.close()

    tensor_feature = torch.Tensor(list_feature).view([len(list_feature), 1, 15, 15])
    tensor_th = torch.Tensor(list_th)
    return tensor_feature, tensor_th


class trainSets(Dataset):
    list_feature_path = []
    list_th_path = []

    def __init__(self, x, y):
        print("******** trainSet init*********")
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.x)

    def __getitem__(self, item):
        return self.x[item], self.y[item]


# trainSet=MyTrainset()   # 实例化该类

tensor_features, tensor_ths = getDataTensor(5)
trainsets = trainSets(tensor_features, tensor_ths)
dataloader = DataLoader(dataset=trainsets, batch_size=BATCH_SIZE, shuffle=True)


class VAE(nn.Module):
    def __init__(self):
        super(VAE, self).__init__()
        self.fc1 = nn.Linear(225, 512)
        self.fc21 = nn.Linear(512, 20)
        self.fc22 = nn.Linear(512, 20)
        self.fc3 = nn.Linear(20, 512)
        self.fc4 = nn.Linear(512, 225)

    def encode(self, x):
        h1 = F.leaky_relu(self.fc1(x))
        return self.fc21(h1), self.fc22(h1)

    def decode(self, z):
        dh1 = F.leaky_relu(self.fc3(z))
        return F.tanh(self.fc4(dh1))

    def reparametrize(self, mu, logvar):
        std = logvar.mul(0.5).exp_()
        if torch.cuda.is_available():
            eps = torch.cuda.FloatTensor(std.size()).normal_()
        else:
            eps = torch.FloatTensor(std.size()).normal_()
        eps = Variable(eps)
        return eps.mul(std).add_(mu)

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparametrize(mu, logvar)
        return self.decode(z), mu, logvar


model = VAE()
if torch.cuda.is_available():
    model.cuda()

reconstruction_function = nn.MSELoss(size_average=False)


def loss_function(recon_x, x, mu, logvar):
    """
    recon_x: generating images
    x: origin images
    mu: latent mean
    logvar: latent log variance
    """
    BCE = reconstruction_function(recon_x, x)  # mse loss
    KLD_element = mu.pow(2).add_(logvar.exp()).mul_(-1).add_(1).add_(logvar)
    KLD = torch.sum(KLD_element).mul_(-0.5)
    # KL divergence
    return BCE + KLD


optimizer = optim.Adam(model.parameters(), lr=LR)
# optimizer = optim.SGD(model.parameters(), lr=LR)

for epoch in range(num_epochs):
    model.train()
    train_loss = 0
    # print(dataloader)
    for batch_idx, data in enumerate(dataloader):  # batch_idx为批次序号，20*10=200，batch_idx最大为20
        img, label = data
        img = img.view(img.size(0) * img.size(1), -1)
        # print(img.size())        # torch.Size([10, 225])
        img = Variable(img)
        if torch.cuda.is_available():
            img = img.cuda()
        optimizer.zero_grad()
        recon_batch, mu, logvar = model(img)
        loss = loss_function(recon_batch, img, mu, logvar)
        loss.backward()
        train_loss += loss.item()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch,
                batch_idx * len(img),
                len(dataloader.dataset), 100. * batch_idx / len(dataloader),
                loss.item() / len(img)))

    print('====> Epoch: {} Average loss: {:.4f}'.format(
        epoch, train_loss / len(dataloader.dataset)))

torch.save(model.state_dict(), './vae.pth')
end_time = time.time()
print("耗时:%d" % ((end_time - start_time) / 60) + "分钟")
