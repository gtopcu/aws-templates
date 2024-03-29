# https://www.youtube.com/watch?v=iGFdh6_FePU

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt 

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

# np.sort(random)
# np.arange(0, 10, 1)
# np.random.randint(0, 100, 10)
# np.random.randn(4)        # 4 x 1 matrix
# np.random.randn(4, 3)     # 4 x 3 matrix
# np.random.shuffle(lst)
# np.random.choice(lst)
# np.random.seed(1)
# np.random.bytes(32)
# np.random.normal(loc=mean, scale, size) # gaussian

# create random data
# xdata = np.random.random([2, 4])  # 2x4 array
# xdata1 = xdata[0, :]              # 1st row
# xdata2 = xdata[1, :]              # 2nd row

# print(np.array([0, 6]).mean())
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# print(np.mean(speed))
# print(np.median(speed))
# print(stats.mode(speed))


# ----------------------------------------------------------------------------------------------------
# Pandas - Series
# print(pd.__version__)

# series = pd.Series(np.random.randn(4), name="PD Series'")
# series.index = ["2020", "2021", "2022", "2023"]
# print(series["2020"])
# series["2020"] = 0.09012
# print("2020" in series)
# print(series)
# print(series.abs())
# print(series * 100)
# print(series.describe())
# series.dtype 
# series.dtypes
# series.items
# series.keys
# series.values
# series.at
# series.loc 
# series.iloc
# series.array
# series.count
# series.is_monotonic_increasing

# series.copy()
# series.add()
# series.any()
# series.mean()
# series.median()
# series.searchsorted()
# series.to_excel("series.xlsx")
# series.to_csv("series.csv")
# series.to_numpy()
# series.to_sql()
# series.to_json()
# series.to_nump()
# series.to_frame()
# series.to_dict()

# ------------------------------------------------------------------------------------------------
# Pandas - DataFrame

# pd.core.Frame.DataFrame
# df = pd.DataFrame(np.random.randn(4, 3), columns=["A", "B", "C"])
# df = pd.DataFrame({ 'month': [1, 4, 7, 10],
#                     'year': [2012, 2014, 2013, 2014],
#                     'sale': [55, 40, 84, 31]}
#                 )
# df = pd.read_csv("data.csv", sep=';')

# data:list[str] = requests.get("http://data.csv").content.decode().split("\n")
# df = pd.read_csv("data.csv", index_col = 0, parse_dates=True, delimiter=" ",  sep=';')

# df.size
# df.columns = ["2021", "2022", "2023"]
# df.dtypes

# print(df.describe())
# df.index
# df.set_index("A", inplace=True)

# print(df)
# print(df.head(2))
# df.tail(2)
# df["D"] = df["A"] * 2 / df["B"]
# print(df[2:4])            # rows 2:4
# print(df[["A", "B"]])     # columns A and B

# print(df.iloc[0])         # First row
# print(df.iloc[0:2])       # first two rows
# print(df.iloc[:3])        # first three rows
# print(df.iloc[1,2])       # element at row 1 and column 2
# print(df.iloc[2:4, 1:3])  # rows 2:4 and columns 1:3

# print(df.loc[2:4, "B"])                   # rows 2:4 and column B
# print(df.loc[df.index[1:3], ["C", "B"]])  # rows 1:3 and columns C and B
# df.loc[df.index[1:3], ["C", "B"]] = 0
# df.loc[df.index[1:3], ["C", "B"]] = np.random.randn(2, 2)

# df = df.sort_values(by="A", ascending=False)
# df.sort_index(axis=1, ascending=False, inplace=True)

# %matplotlib inline
# df.plot(title="Plot Data", grid=True, legend=True, subplots=True, logx=False, logy=False) # line plot
# df["A"].plot(kind="bar") # 'line', 'bar', 'barh', 'hist', 'box', 'kde', 'density', 'area', 'pie', 'scatter', 'hexbin'
# plt.show()

# df.to_csv("dataframe.csv")
# df.to_excel("dataframe.xlsx")
# df.to_json("dataframe.json")
# df.to_sql("dataframe")
# df.to_numpy()

# pd.set_option("precision", 1)
# pd.set_option("display.max_columns", 500)
# pd.set_option("display.rows", 20)
# pd.set_option("display.width", 1000)
# pd.set_option("display.max_colwidth", -1)


