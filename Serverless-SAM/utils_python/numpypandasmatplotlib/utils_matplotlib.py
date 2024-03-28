
# https://matplotlib.org/stable/gallery/color/named_colors.html
# https://www.w3schools.com/python/matplotlib_line.asp

import matplotlib.pyplot as plt 
import numpy as np

from typing import Sequence

import math

#------------------------------------------------------------------------------------------------
# Line Chart

# xpoints = np.array([1, 8]) # optional
# ypoints = np.array([3, 10])

# plt.plot(x, y, color='r', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)
# plt.plot(xpoints, ypoints)
# plt.plot(xpoints, ypoints, 'o') # without line
# plt.show()

# plt.grid()
# plt.legend()
# plt.pause(0.01)
# plt.clf()
# plt.figure(figsize=(8, 4))

#------------------------------------------------------------------------------------------------
# Line Chart - 2

# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linestyle = 'dotted', marker = 'o') # auto x-axis
# plt.show()

#------------------------------------------------------------------------------------------------
# Bar Chart

# lst = np.random.randint(0, 100, 10)
# x = np.arange(0, 10, 1)

# plt.title("Matplotlib Chart")
# plt.bar(x, lst, color='r', label="growth")
# plt.show()

#-----------------------------------------------------------------------------------------------
# Pie Chart

# lst = np.random.randint(0, 100, 5)
# labels: Sequence[str] = ["A", "B", "C", "D", "E"] # list/tuple

# plt.pie(lst, labels=labels, autopct="%1.1f%%")
# plt.show()

#-----------------------------------------------------------------------------------------------
# Scatter Plot

# plt.scatter(np.random.randint(0, 100, 50), np.random.randint(0, 100, 50), c=np.random.randint(0, 100, 50), cmap="Blues")
# plt.show()

#-----------------------------------------------------------------------------------------------
# Histogram

# x = np.random.normal(35, 20, 100) # Mean, standard deviation, count
# plt.hist(x)
# plt.show() 


#-----------------------------------------------------------------------------------------------


# x = np.arange(1, 5, 1)

# # O(1)
# y = [1 for i in x]
# plt.plot(x, y, color='c', linestyle='dashed', linewidth=2, label="constant")

# # O(logn)
# y = [math.log(i) for i in x]
# plt.plot(x, y, color='r', linestyle='dashed', linewidth=2, label="logarithmic")

# # O(n)
# y = [i for i in x]
# plt.plot(x, y, color='b', linestyle='dashed', linewidth=2, label="linear")

# # O(nlogn)
# y = [(i * math.log(i)) for i in x]
# plt.plot(x, y, color='g', linestyle='dashed', linewidth=2, label="quasilinear")

# # O(n^2)
# y = [i**2 for i in x]
# plt.plot(x, y, color='y', linestyle='dashed', linewidth=2, label="quadratic")

# # O(2^n)
# y = [2**i for i in x]
# plt.plot(x, y, color='m', linestyle='dashed', linewidth=2, label="exponential")

# # O(n!)
# y = [math.factorial(i) for i in x]
# plt.plot(x, y, color='k', linestyle='dashed', linewidth=2, label="factorial")

# plt.grid(visible=True, which='major', axis='both', linestyle='--')
# plt.legend()
# plt.plot()
# plt.show()

