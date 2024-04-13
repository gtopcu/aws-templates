

# https://pytorch.org/tutorials/beginner/introyt/introyt1_tutorial.html 
# https://pytorch.org/get-started/locally/

import torch

# x = torch.rand(5, 3)
# print(x)

# z = torch.zeros(5, 3)
# z.dtype
# i = torch.ones((5, 3), dtype=torch.int16)
# i.dtype

# torch.manual_seed(1729)
# r1 = torch.rand(2, 2)
# r2 = torch.rand(2, 2)
# torch.manual_seed(1729)
# r3 = torch.rand(2, 2) # same as r1 as same seed

# ones = torch.ones(2, 3)
# twos = torch.ones(2, 3) * 2
# threes = ones + twos
# threes.shape

# r = torch.rand(2, 2) - 0.5 * 2 # numbers between -1 and 1
# torch.abs(r)
# torch.asin(r)       # arcsine
# torch.det(r)        # determinant
# torch.svd(r)        # single value decomposition
# torch.std_mean(r)
# torch.max(r)


# Autograd
x = torch.randn(1, 10)
prev_h = torch.rand(1, 20)
W_h = torch.rand(20, 20)
W_x = torch.rand(20, 10)

i2h = torch.mm(W_x, x.t())
h2h = torch.mm(W_h, prev_h.t())
next_h = i2h + h2h
next_h = next_h.tanh()

loss = next_h.sum()
loss.backward()



