# -*- coding: utf-8 -*-
import torch
import torch.nn
from torch.nn import Tanh
import torch.nn.functional as nn
import torch.autograd as autograd
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

from tensorflow.python.ops.gen_nn_ops import LeakyRelu
from torch.autograd import Variable
from tensorflow.examples.tutorials.mnist import input_data

# 1.读取datasets

# 2.定义批大小、解码后维度大小(张量)、矩阵大小、隐藏层神经元个数等参数

# 批大小


batch_size = 10
# 输入层
x_dim = 36
# 隐藏层
h_dim = 512
# 第二隐藏层
h2_dim = 256
# 解码输出层
z_dim = 2
# 计数变量
cnt = 0
# 学习速率
lr = 1e-3

# 3.编码器、解码器、判断器

# Encoder
Enc = torch.nn.Sequential(
    torch.nn.Linear(x_dim, h_dim),  # 输入样本特征数量、输出样本特征数量
    torch.nn.LeakyReLU(),  # 带泄露修正线性单元（隐层激活函数）
    torch.nn.Linear(h_dim, h_dim),
    torch.nn.BatchNorm1d(512),
    torch.nn.LeakyReLU(),
    torch.nn.Linear(h_dim, z_dim)
)
# Decoder
Dec = torch.nn.Sequential(
    torch.nn.Linear(z_dim, h_dim),
    torch.nn.LeakyReLU(),  # （隐层激活函数）
    torch.nn.Linear(h_dim, h_dim),
    torch.nn.BatchNorm1d(512),
    torch.nn.LeakyReLU(),
    torch.nn.Linear(h_dim, x_dim),
    torch.nn.Tanh(),
    torch.nn.Sigmoid()

)
# Discriminator
Dis = torch.nn.Sequential(
    torch.nn.Linear(z_dim, h_dim),
    torch.nn.LeakyReLU(),
    torch.nn.Linear(h_dim, h2_dim),
    torch.nn.LeakyReLU(),
    torch.nn.Linear(h2_dim, 1),
    torch.nn.Sigmoid()
)


def reset_grad():
    Enc.zero_grad()
    Dec.zero_grad()
    Dis.zero_grad()
