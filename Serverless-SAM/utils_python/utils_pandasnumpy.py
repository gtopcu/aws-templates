# https://www.youtube.com/watch?v=iGFdh6_FePU

import pandas as pd
import numpy as np
from scipy import stats

# print(np.array([0, 6]).mean())
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# print(np.mean(speed))
# print(np.median(speed))
# print(stats.mode(speed))

# series = pd.Series(np.random.randn(4), name="PD Series'")
# print(series)
# print(np.abs(series))
# print(series * 100)
# print(series.describe())


data = pd.read_csv("data.csv", sep=';')
pd.set_option("display.max_columns", 500)
pd.set_option("display.rows", 20)
pd.set_option("display.width", 1000)
data.iloc[2:4, 1:3]

