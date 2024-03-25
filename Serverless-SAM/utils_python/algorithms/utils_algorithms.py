
# https://www.youtube.com/watch?v=IRkvlqPBqNg

import pandas as pd
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt 

import time
import random


#------------------------------------------------------------------------------
# Bubble Sort
# Best case O(n) if sorted, worst case 0(n^2) 

COUNT = 10
MAX = 100
counter = 0

lst = np.random.randint(0, MAX, COUNT)
x = np.arange(0, COUNT, 1)

n = len(lst)
for i in range(n):
    for j in range(0, n-i-1):
        print(i, j)
        counter += 1
        plt.bar(x, lst, color='r')
        plt.pause(0.01)
        plt.show(block=False)
        plt.clf()
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("done:", counter)


#------------------------------------------------------------------------------
# Merge Sort
# Best/worst case O(n*log(n))

# random.seed("ABC")
# numbers = [random.randint(0, 1000) for _ in range(20)] 
# print(numbers)

# def merge_sort(number_list, left, right):
#     # base case
#     if left >= right:
#         return
    
#     # find the middle
#     mid = (left + right) // 2

#     # split recursively into left and right halves
#     merge_sort(number_list, left, mid)
#     merge_sort(number_list, mid + 1, right)

#     # merge the two results
#     merge(number_list, left, mid, right)


# def merge(number_list, left, mid, right):

#     # create two temporary lists to store the two halves
#     left_list = number_list[left:mid + 1]
#     right_list = number_list[mid + 1:right + 1]

#     # initialize the indices for the left and right lists
#     left_index = 0
#     right_index = 0

#     # initialize the index for the merged list
#     merged_index = left

#     # merge the two lists
#     while left_index < len(left_list) and right_index < len(right_list):
#         if left_list[left_index] <= right_list[right_index]:
#             number_list[merged_index] = left_list[left_index]
#             left_index += 1
#         else:
#             number_list[merged_index] = right_list[right_index]
#             right_index += 1
#         merged_index += 1

#     # copy any remaining elements from the left list
#     while left_index < len(left_list):
#         number_list[merged_index] = left_list[left_index]
#         left_index += 1
#         merged_index += 1

# merge_sort(numbers, 0, len(numbers) - 1)
# print(numbers)
# print("done")


#------------------------------------------------------------------------------
# Quicksort 
# Average O(n*log(n)) - quicker than Merge Sort, Bubble Sort, and other sorting algorithms
# Worst-case time complexity is O(n^2)
# Based on the divide and conquer approach. Works by selecting a pivot element from the array, 
# partitioning the other elements into two subarrays, and recursively sorting the subarrays.

