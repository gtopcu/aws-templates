
# https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html

# pip install torch==2.2.2
# pip install torchvision==0.17.2

# %matplotlib inline

import torch
from torch import Tensor
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

# print(torch.cuda.is_available())

# 1 dimension: Vector
# 2 dimensions: Matrix
# 3+ dimensions: Tensor

# creates a copy from tuple/list
# tensor_from_tuple = torch.tensor((0, 1, 2))
# tensor_from_lists = torch.tensor([ [0, 1, 2], [3, 4, 5] ])

# vector = torch.rand(6)
# print(vector)

# i = torch.ones((5, 3), dtype=torch.int16)
# print(i.dtype)

# r0 = torch.empty(2, 2)
# r1 = torch.ones(2, 2)

# torch.manual_seed(1729)
# torch.rand(2, 2)              # 0 to 1
# torch.randn(2, 2)             # -1 to 1
# torch.rand(2, 2) - 0.5 * 2    # numbers between -1 and 1

# ones = torch.ones(2, 3)
# twos = torch.ones(2, 3) * 2
# threes = ones + twos
# threes.shape

# torch.empty_like(x)
# torch.zeros_like(x)
# torch.ones_like(x)

# torch.arange(0, 100, 1)
# torch.abs(r)
# torch.asin(r)       # arcsine
# torch.det(r)        # determinant
# torch.svd(r)        # single value decomposition
# torch.std_mean(r)
# torch.max(r)

# DataTypes
# torch.bool
# torch.int8
# torch.uint8
# torch.int16
# torch.int32
# torch.int64
# torch.half
# torch.float
# torch.float16
# torch.float32  - default
# torch.float64
# torch.double
# torch.bfloat16

# matrix_f32 = torch.randn((2, 2), dtype=torch.float32) * 10
# print(matrix_f32)
# matrix_i32 = matrix_f32.to(torch.int32)
# print(matrix_i32)

# Dataset stores the samples and their corresponding labels
# DataLoader wraps an iterable around the Dataset



