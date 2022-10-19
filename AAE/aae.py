# -*- coding: utf-8 -*-
import torch
import torch.nn
import torch.nn.functional as nn
import torch.autograd as autograd
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os
from torch.autograd import Variable
from tensorflow.examples.tutorials.mnist import input_data

# from torchvision.datasets import MINST

mnist = input_data.read_data_sets('../../MNIST_data', one_hot=True)

# mnist = MINST('./data', download=True)
mb_size = 32
# z_dim = 5
z_dim = 2
# X_dim = mnist.train.images.shape[1]
X_dim = mnist.train.images.shape[1]
print("X_dim= ", X_dim)  # 784
y_dim = mnist.train.labels.shape[1]
print("h_dim= ", y_dim)  # 10
h_dim = 128
cnt = 0
lr = 1e-3

# Encoder
Q = torch.nn.Sequential(
    torch.nn.Linear(X_dim, h_dim),
    torch.nn.ReLU(),
    # torch.nn.Linear(h_dim, h_dim),
    # torch.nn.BatchNorm1d(128),
    # torch.nn.LeakyReLU(),
    torch.nn.Linear(h_dim, z_dim)
)

# Decoder
P = torch.nn.Sequential(
    torch.nn.Linear(z_dim, h_dim),
    torch.nn.ReLU(),
    # ##
    # torch.nn.Linear(h_dim, h_dim),
    # torch.nn.BatchNorm1d(128),
    # torch.nn.LeakyReLU(),
    # ##
    # torch.nn.Linear(h_dim, X_dim),
    # torch.nn.Tanh(),
    torch.nn.Sigmoid()
)

# Discriminator
D = torch.nn.Sequential(
    torch.nn.Linear(z_dim, h_dim),
    torch.nn.ReLU(),
    # torch.nn.Linear(h_dim, h2_dim),
    # torch.nn.LeakyReLU(),
    # torch.nn.Linear(h2_dim, 1),
    torch.nn.Sigmoid()
)


def reset_grad():
    Q.zero_grad()
    P.zero_grad()
    D.zero_grad()


def sample_X(size, include_y=False):
    X, y = mnist.train.next_batch(size)
    X = Variable(torch.from_numpy(X))

    if include_y:
        y = np.argmax(y, axis=1).astype(np.int)
        y = Variable(torch.from_numpy(y))
        return X, y

    return X


# params(iterable)：可用于迭代优化的参数或者定义参数组的dicts。
# lr (float, optional) ：学习率(默认: 1e-3)
Q_solver = optim.Adam(Q.parameters(), lr=lr)
P_solver = optim.Adam(P.parameters(), lr=lr)
D_solver = optim.Adam(D.parameters(), lr=lr)

for it in range(1000000):
    X = sample_X(mb_size)

    """ Reconstruction phase """
    z_sample = Q(X)
    X_sample = P(z_sample)

    recon_loss = nn.binary_cross_entropy(X_sample, X)

    recon_loss.backward()
    P_solver.step()
    Q_solver.step()
    reset_grad()

    """ Regularization phase """
    # Discriminator
    z_real = Variable(torch.randn(mb_size, z_dim))  # torch.randn(mb_size, z_dim)为标准正态分布
    print(z_real)  # 张量值
    z_fake = Q(X)

    D_real = D(z_real)
    D_fake = D(z_fake)

    D_loss = -torch.mean(torch.log(D_real) + torch.log(1 - D_fake))

    D_loss.backward()
    D_solver.step()
    reset_grad()

    # Generator
    z_fake = Q(X)
    D_fake = D(z_fake)

    G_loss = -torch.mean(torch.log(D_fake))

    G_loss.backward()
    Q_solver.step()
    reset_grad()

    # Print and plot every now and then
    if it % 1000 == 0:
        print('Iter-{}; D_loss: {:.4}; G_loss: {:.4}; recon_loss: {:.4}'

              .format(it, D_loss.data, G_loss.data, recon_loss.data))

        samples = P(z_real).data.numpy()[:16]

        fig = plt.figure(figsize=(4, 4))
        gs = gridspec.GridSpec(4, 4)
        gs.update(wspace=0.05, hspace=0.05)

        for i, sample in enumerate(samples):
            ax = plt.subplot(gs[i])
            plt.axis('off')
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.set_aspect('equal')
            plt.imshow(sample.reshape(28, 28), cmap='Greys_r')  # 白黑色

        if not os.path.exists('out/'):
            os.makedirs('out/')

        plt.savefig('out/{}.png'
                    .format(str(cnt).zfill(3)), bbox_inches='tight')  # zfill表示字符串以width位数对齐，前面填充0
        cnt += 1
        plt.close(fig)
