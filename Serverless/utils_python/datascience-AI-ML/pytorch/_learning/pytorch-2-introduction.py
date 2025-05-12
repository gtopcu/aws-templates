

# https://pytorch.org/tutorials/beginner/introyt/introyt1_tutorial.html 
# https://pytorch.org/get-started/locally/

import torch


# Autograd
# x = torch.randn(1, 10)
# prev_h = torch.rand(1, 20)
# W_h = torch.rand(20, 20)
# W_x = torch.rand(20, 10)

# i2h = torch.mm(W_x, x.t())
# h2h = torch.mm(W_h, prev_h.t())
# next_h = i2h + h2h
# next_h = next_h.tanh()

# loss = next_h.sum()
# loss.backward()


###################################################################################################
# Building Models
###################################################################################################

# import torch
# import torch.nn as nn
# import torch.nn.functional as F

# class LeNet(nn.Module):

#     def __init__(self):
#         super(LeNet, self).__init__()
#         # 1 input image channel (black & white), 6 output channels, 3x3 square convolution
#         # kernel
#         self.conv1 = nn.Conv2d(1, 6, 3)
#         self.conv2 = nn.Conv2d(6, 16, 3)
#         # an affine operation: y = Wx + b
#         self.fc1 = nn.Linear(16 * 6 * 6, 120)  # 6*6 from image dimension
#         self.fc2 = nn.Linear(120, 84)
#         self.fc3 = nn.Linear(84, 10)

#     def forward(self, x):
#         # Max pooling over a (2, 2) window
#         x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
#         # If the size is a square you can only specify a single number
#         x = F.max_pool2d(F.relu(self.conv2(x)), 2)
#         x = x.view(-1, self.num_flat_features(x))
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = self.fc3(x)
#         return x

#     def num_flat_features(self, x):
#         size = x.size()[1:]  # all dimensions except the batch dimension
#         num_features = 1
#         for s in size:
#             num_features *= s
#         return num_features


# if __name__ == "__main__":
#     net = LeNet()
#     print(net)
#     input = torch.rand(1, 1, 32, 32) # stand-in for a 32x32 black & white image
#     print("Image batch shape:", input.shape)
#     output = net(input)
#     print("Raw output: ")
#     print(output)
#     print("Output shape:", output.shape)


###################################################################################################
# Datasets and Loaders
###################################################################################################

# # %matplotlib inline
# import torch
# import torchvision
# import torchvision.transforms as transforms
# # from torch.utils.data import Dataset, DataLoader
# # from torchvision.datasets import ImageFolder

# transform = transforms.Compose(
#     [transforms.ToTensor(),
#      transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

# trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
# trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

# import numpy as np
# from matplotlib import pyplot as plt

# def imshow(imb):
#     img = img / 2 + 0.5
#     npimg = img.numpy()
#     plt.imshow(np.transpose(npimg, (1, 2, 0)))

# dataiter = iter(trainloader)
# images, labels = dataiter.next()
# imshow(torchvision.utils.make_grid(images))
# print(' '.join('%5s' % classes[labels[j]] for j in range(4)))













