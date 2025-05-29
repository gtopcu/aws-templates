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
# arr.reshape(3. 2, -1) -> only one dimension can be -1
# arr.reshape(-1)       -> flatten

# arr.dtype     # array's data type
# arr.ndim      # array's no of dimensions
# arr.shape     # array's shape, tuple i.e. (2, ), (2, 3) etc

# print('Last element from 2nd dim: ', arr[1, -1])

# arr = np.array([1, 2, 3, 4], dtype='S')
# arr = np.array([1, 2, 3, 4], dtype='i4') #int32

# converting data type
# newarr = arr.astype(int)
# newarr = arr.astype('i') 
# newarr = arr.astype(bool)

# copy(does not affect original)/view
# x = arr.copy()
# x = arr.view()

# https://numpy.org/doc/stable/reference/generated/numpy.greater.html
# all() | any()
# A.shape == B.shape
# (A==B).all()                  # elements are equal
# (A==B).array_equal()          # elements and shape are equal
# (A==B).allclose() | isClose() # https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose

# pd.Series(arr.flatten()).plot(kind='hist', bins=50, title='Histogram')
# plt.show()

# print(np.array((2, 2), dtype=np.int64))
# np.empty(2, 2)
# np.zeros((2,2), np.int32)
# np.ones((3, 3), np.float32)   # 3 x 3 matrix consisting of 1s with float32 data type
# np.empty_like(x)
# np.zeros_like(x)
# np.ones_like(x)
# np.arange(0, 10, 1)
# np.random.randint(0, 100, 10)
# np.random.rand(4)            # 4 x 1 matrix (0-to-1)
# np.random.randn(4)           # 4 x 1 matrix (-1-to-1)
# np.random.rand(4, 3)         # 4 x 3 matrix (0-to-1)
# np.random.shuffle(lst)
# np.random.choice(lst)
# np.random.seed(1)
# np.random.bytes(32)
# np.random.normal(loc=mean, scale, size) # gaussian
# np.sort(random)
# np.unique(y)
# x = np.where(arr%2 == 0)

# create random data
# xdata = np.random.random([2, 4])      # 2x4 array
# xdata = xdata[0, :]                   # 1st row
# xdata = xdata[1, :]                   # 2nd row
# xdata = xdata[:,:,0]                  # 1st row in the 3rd dimension 
# xdata = xdata[ … , 0]                 # 1st row in the last dimension
# array = np.random.rand(2, 2, 2, 2)
# print(array[..., 0])
# print(array[Ellipsis, 0])

# print(np.array([0, 6]).mean())
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# print(np.mean(speed))
# print(np.median(speed))
# print(stats.mode(speed))


# ----------------------------------------------------------------------------------------------------
# Pandas - Series
# print(pd.__version__)

# series = pd.Series(np.random.randn(4), name="PD Series")
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
# series.to_numpy()
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

# data:list[str] = requests.get("http://data.csv").content.decode().split("\n")

# df = pd.read_csv("data.csv", sep=';')
# df = pd.read_csv("data.csv", index_col = 0, parse_dates=True, delimiter=" ",  sep=';')
# pd.read_clipboard | pd.read_excel | pd.read_json| pd.read_parquet| pd.read_pickle | pd.read_sql | pd.read_hdf
# pd.to_csv() | pd.to_numpy| to_clipboard | pd.to_excel | pd.to_json | pd.to_parquet | pd.to_pickle | pd.to_sql | pd.to_hdf

# df = pd.DataFrame(np.random.randn(4, 3), columns=["A", "B", "C"], index=["a", "b", "c", "d"])
# df = pd.DateFrame(iterable)

# df
# df.size   
# df.shape  # (16598, 11)
# df.dtypes | df.printSchema()
# df.index
# df.values
# df.columns = ["column1", "column2"]

# df.describe()
# df.set_index("id", inplace=True)
# df.show()

# df.show()
# df.head(2)
# df.tail(2)
# df.set_index("id")["title"].to_dict()
# df["columnName"] | df.columnName
# df["D"] = df["A"] * 2 / df["B"]
# df["create_date"] = dt.datetime.now()
# df["salary"] = df["salary"] + 1_000_000
# df["salary"] = df["salary"].apply(lambda x: x * 2)
# df[2:4]               # rows 2:4
# df["genre"]           # genre column
# df[["A", "B"]]        # columns A and B
# len(df.ids.unique())       # no of unique items
# X = df.drop(columns=["genre"]) # drop column and return the rest, does not modify original
# X = df.dropna()       # drop missing values
# df = df.sort_values(by="A", ascending=False)
# df.sort_index(axis=1, ascending=False, inplace=True)

# df.all() df.any() df.median() df.max() df.min() df.count() df.abs() df.map(), df.first()
# df.keys() df.values() df.items() df.assign() df.reset_index()
# df.filter() | df.select()
# df.agg(["min", "max", "mean"])["A"].values
# df.apply(lambda row: row["A"] * 2, axis=1)

# for idx, row in df.iterrows():
# df.at[0, "A"] = 0
# df.iloc[0]          # First row
# df.iloc[0:2]        # first two rows
# df.iloc[:3]         # first three rows
# df.iloc[1,2]        # element at row 1 and column 2
# df.iloc[2:4, 1:3]   # rows 2:4 and columns 1:3

# df.loc[2:4, "B"]                    # rows 2:4 and column B
# df.loc[df.index[1:3], ["C", "B"]]   # rows 1:3 and columns C and B
# df.loc[df.index[1:3], ["C", "B"]] = 0
# df.loc[df.index[1:3], ["C", "B"]] = np.random.randn(2, 2)

# Can use SQL on DFs
# import pandasql as ps
# ps.sqldf("SELECT * FROM df WHERE A > 0 and B < 0", locals())
# sql_query = SELECT * FROM data df LEFT JOIN df2 ON df.id = df2.id WHERE df.A > 0
# ps.sqldf(sql_query, locals())

# df.query("A > 0 and gender = 'f'", inplace=True)
# df.select("*")
# df.select("A", "B").where("A > 0").limit(10).groupby("A").sum().orderby("A", ascending=False).distinct()
# df.where((df.Age > 30) & (df.Type == 1) & df.Job.isin(["student", "doctor"])).limit(5).show(10)
# df.groupby(["emp_no", "name"])["salary"].max().alias("SalaryMax")
# average_sales_per_agent = df.groupby('Agent')['Total Sale Price'].mean()

# DF to Spark RDD
# df.rdd

# df.plot(title="Plot Data", grid=True, legend=True, subplots=True, logx=False, logy=False) # line plot
# df["A"].plot(kind="bar") # 'line', 'bar', 'barh', 'hist', 'box', 'kde', 'density', 'area', 'pie', 'scatter', 'hexbin'
# df
# plt.show()


############################################################################################################
# Reading/Writing directly from MySQL -> .ipynb
# https://www.youtube.com/watch?v=DiQ5Hni6oRI
# import pandas as pd
# import sqlalchemy
# from sqlalchemy import create_engine
# print("Alchemy version", sqlalchemy.__version__)
# query = """
#         SELECT name, birthday FROM employees e
#         JOIN salaries s ON e.id = s.id
#         WHERE s.salary > 100000
# """
# engine = create_engine('mysql+pymysql:///user:pwd@localhost/dbname', echo=True)
# df = pd.read_sql(query, con=engine)
# df.groupby(["emp_no", "name"])["salary"].max().reset_index()
# df

