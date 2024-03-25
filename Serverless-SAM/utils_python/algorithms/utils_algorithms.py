
# https://www.youtube.com/watch?v=IRkvlqPBqNg
# https://www.youtube.com/watch?v=AAwYzYkjNTg

import pandas as pd
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt 

import time
import random


#------------------------------------------------------------------------------
"""

Binary Trees - O(log n) avg, O(n) worst case
Breadh-First Search (BFS)
Depth-First Search (DFS)
ALV Tables: Self balancing binary search trees, guarantees O(log n) for search, insert, delete


"""
#------------------------------------------------------------------------------
# Dynamic Programming: Recursive, Memoized, Bottom-Up
# https://www.youtube.com/watch?v=vYquumk4nWw&t=372s

# Fibo
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584...

# 1- Recursive Solution: O(2^n)
def fibo(x: int) -> int:
    return x if x < 2 else fibo(x-1) + fibo(x-2)
# print(fibo(5))

# 2- Memoized Solution: O(n)
def fibo_mem(x: int) -> int:
    cache = { 0:0, 1:1}
    def _fibo(x: int) -> int:
        if x not in cache:
            cache[x] = _fibo(x-1) + _fibo(x-2)
        return cache[x]
    return _fibo(x)
# print(fibo_mem(4))

# 3- Bottom-Up Solution: O(n)
def fibo_bottomup(x: int) -> int:
    fibo_list = [0] * (x+1)
    fibo_list[0] = 0
    fibo_list[1] = 1
    for i in range(2, x+1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    return fibo_list[x]
# print(fibo_bottomup(6))

number = 40
start = time.time()
# print(fibo(number))           # 9.224573s  
# print(fibo_mem(number))       # 0.000022s
print(fibo_bottomup(number))    # 0.000022s
print(f"Total: {(time.time() - start):.6f}s")
# print(f"{number:.5f}")

#------------------------------------------------------------------------------
# Bubble Sort
# Best case O(n) if sorted, worst case 0(n^2) 

# COUNT = 10
# MAX = 100

# lst = np.random.randint(0, MAX, COUNT)
# x = np.arange(0, COUNT, 1)

# counter = 0
# for i in range(COUNT):
#     for j in range(0, COUNT-i-1):
#         print(i, j)
#         counter += 1
#         plt.bar(x, lst, color='r')
#         plt.pause(0.1)
#         plt.show(block=False)
#         plt.clf()
#         if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
# print("done:", counter)


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

