
# https://www.youtube.com/watch?v=RfXt_qHDEPw
# https://www.youtube.com/watch?v=IRkvlqPBqNg
# https://www.youtube.com/watch?v=AAwYzYkjNTg
# https://www.youtube.com/watch?v=oz9cEqFynHU
# https://www.youtube.com/watch?v=kp3fCihUXEg
# https://www.youtube.com/watch?v=cQWr9DFE1ww 


import numpy as np
import matplotlib.pyplot as plt 
import time
import random

#------------------------------------------------------------------------------
"""

Worst to best:
-----------------------------------
O(n!)       -> Factorial
O(2^n)      -> Exponential
O(n^2)      -> Quadratic 
O(n*log(n)) -> Quasilinear
O(n)        -> Linear
O(log n)    -> Logarithmic
O(1)        -> Constant
-----------------------------------

Binary Search(Trees/Graphs) -> O(log n) avg, O(n) worst case
Breadh-First Search (BFS)   -> O(n+b) : O(n)
Depth-First Search (DFS)    -> O(n+b) : O(n)
ALV Tables: Self balancing binary search trees, guarantees O(log n) for search, insert, delete

Simple -> O(n) best, O(n^2) avg/worst
Binary, Binary Insertion, Insertion, Selection, Double Selection, Bubble, Shaker    
                                                                        
Divide & Conquer -> O(n*log(n))
Quicksort, Merge Sort, Heapsort, Radix Sort, Bucket Sort, Shell Sort, Tim Sort, Pigeonhole Sort


"""
start = time.time()

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

# number = 40
# start = time.time()
# print(fibo(number))           # 9.224573s  
# print(fibo_mem(number))       # 0.000022s
# print(fibo_bottomup(number))    # 0.000022s
# print(f"Total: {(time.time() - start):.6f}s")
# print(f"{number:.5f}")

#------------------------------------------------------------------------------
# Binary Search
# Avg 0(log n)
# Collection must be sorted!

def binary_search(lst: list, value: int) -> int:
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

list = [*range(50)]
# random.shuffle(list)
print(binary_search(list, 25))


#------------------------------------------------------------------------------
# Insertion Sort
# Best case O(n) if sorted, worst case 0(n^2)

# def insertion_sort(lst: list) -> list:
#     for i in range(1, len(lst)):
#         key = lst[i]
#         j = i - 1
#         while j >= 0 and key < lst[j]:
#             lst[j+1] = lst[j]
#             j -= 1
#         lst[j+1] = key
#     return lst

# list = [*range(50)]
# random.shuffle(list)
# print(insertion_sort(list))


#------------------------------------------------------------------------------
# Selection Sort
# Best case O(n) if sorted, worst case 0(n^2)

# def selection_sort(lst: list) -> list:
#     for i in range(len(lst)):
#         min_index = i
#         for j in range(i+1, len(lst)):
#             if lst[j] < lst[min_index]:
#                 min_index = j
#         lst[i], lst[min_index] = lst[min_index], lst[i]
#     return lst

# list = [*range(50)]
# random.shuffle(list)
# print(selection_sort(list))

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
# Quicksort - quicker than Merge Sort, Bubble Sort, and other sorting algorithms
# Best/avg O(n*log(n)) worst O(n^2)
# Based on the divide and conquer approach. Works by selecting a pivot element from the array, 
# partitioning the other elements into two subarrays, and recursively sorting the subarrays.

# Quicksort
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)

# list = [*range(50)]
# random.shuffle(list)
# print(quicksort(list))


print(f"Total: {(time.time() - start):.6f}s")