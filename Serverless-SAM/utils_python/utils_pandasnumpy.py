# https://www.youtube.com/watch?v=iGFdh6_FePU

import pandas as pd
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt 

import time
import random


# print(np.array([0, 6]))
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

# data = pd.read_csv("data.csv", sep=';')
# pd.set_option("display.max_columns", 500)
# pd.set_option("display.rows", 20)
# pd.set_option("display.width", 1000)
# data.iloc[2:4, 1:3]


#------------------------------------------------------------------------------
# Sort Algorithms
# https://www.youtube.com/watch?v=IRkvlqPBqNg
#------------------------------------------------------------------------------

# Bubble Sort
# COUNT = 5
# MAX = 10
# 0
# lst = np.random.randint(0, MAX, COUNT)
# x = np.arange(0, COUNT, 1)

# n = len(lst)
# for i in range(n):
#     for j in range(0, n-i-1):
#         print(i, j)
#         plt.bar(x, lst, color='r')
#         plt.pause(0.1)
#         plt.show(block=False)
#         plt.clf()
#         if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
# print("done")


#------------------------------------------------------------------------------
# Merge Sort

random.seed("ABC")
numbers = [random.randint(0, 1000) for _ in range(20)] 
print(numbers)

def merge_sort(number_list, left, right):
    # base case
    if left >= right:
        return
    
    # find the middle
    mid = (left + right) // 2

    # split recursively into left and right halves
    merge_sort(number_list, left, mid)
    merge_sort(number_list, mid + 1, right)

    # merge the two results
    merge(number_list, left, mid, right)


def merge(number_list, left, mid, right):

    # create two temporary lists to store the two halves
    left_list = number_list[left:mid + 1]
    right_list = number_list[mid + 1:right + 1]

    # initialize the indices for the left and right lists
    left_index = 0
    right_index = 0

    # initialize the index for the merged list
    merged_index = left

    # merge the two lists
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            number_list[merged_index] = left_list[left_index]
            left_index += 1
        else:
            number_list[merged_index] = right_list[right_index]
            right_index += 1
        merged_index += 1

    # copy any remaining elements from the left list
    while left_index < len(left_list):
        number_list[merged_index] = left_list[left_index]
        left_index += 1
        merged_index += 1

merge_sort(numbers, 0, len(numbers) - 1)
print(numbers)
print("done")