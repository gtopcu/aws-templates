
# https://www.w3schools.com/python/matplotlib_line.asp

import matplotlib.pyplot as plt 
import numpy as np

from typing import Sequence


#------------------------------------------------------------------------------------------------
# Line Chart

xpoints = np.array([1, 8]) # optional
ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints, 'o') # without line
plt.show()

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