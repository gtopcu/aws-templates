# https://www.youtube.com/watch?v=iGFdh6_FePU

import pandas as pd
import numpy as np
from scipy import stats

"""
 ndarray up to 50x faster than traditional Python lists

    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )

"""

# print(np.__version__)

# array: np.ndarray
# arr = np.array(42)                                                  # 0-Dimentional
# arr = np.array([0, 6])                                              # 1-Dimentional
# arr = np.array([[1, 2, 3], [4, 5, 6]])                              # 2-Dimentional
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])    # 3-Dimentional
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print(arr.dtype)    # array's data type
# print(arr.ndim)     # array's no of dimensions
# print(arr.shape)    # array's shape, tuple i.e. (2, ), (2, 3) etc

# print('Last element from 2nd dim: ', arr[1, -1])
# print(arr[0, 1, 2]) # for 3 dimensions

# Create an array with data type string:
# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)
# For i, u, f, S and U we can define size as well. An array with data type 4 bytes integer:
# arr = np.array([1, 2, 3, 4], dtype='i4') #int32
# print(arr)
# print(arr.dtype)

# converting data type
# newarr = arr.astype(int)
# newarr = arr.astype('i') 
# newarr = arr.astype(bool)

# copy(does not affect original)/view
# x = arr.copy()
# x = arr.view()

# random = np.random.randn(4)
# y = np.random.randint(0, 100, 10)
# x = np.arange(0, 10, 1)
# sorted = np.sort(random)

# print(np.array([0, 6]).mean())
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# print(np.mean(speed))
# print(np.median(speed))
# print(stats.mode(speed))


# ----------------------------------------------------------------------------------------------------
# Pandas

# series = pd.Series(np.random.randn(4), name="PD Series'")
# print(series)
# print(np.abs(series))
# print(series * 100)
# print(series.describe())

# data = pd.read_csv("data.csv", sep=';')
# pd.set_option("display.max_columns", 500)
# pd.set_option("display.rows", 20)
# pd.set_option("display.width", 1000)
# data.iloc[2:4, 1:3]



