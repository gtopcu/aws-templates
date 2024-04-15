
# https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions?s=08

from typing import Tuple, List, Dict, Any, Optional
import time
import math
import numpy as np
import heapq
import random
import sys
import operator
import statistics



class Solution:

    #######################################################################################################################
    # ARRAYS
    #######################################################################################################################
    
    # https://leetcode.com/problems/two-sum/description/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    indices.extend([i, j])
                    return indices            
        return indices
    
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(0, len(prices)-1):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i+1] - min_price > max_profit:
                max_profit = prices[i+1] - min_price
        return max_profit

    # https://leetcode.com/problems/contains-duplicate/description/
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True

    # https://leetcode.com/problems/product-of-array-except-self/
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return [math.prod(nums[0:i]) * math.prod(nums[i+1:]) for i in range(len(nums))]
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output

    # https://leetcode.com/problems/k-closest-points-to-origin/
    # kClosest: distance between two points on the X-Y plane is the Euclidean distance 
    # √(x1 - x2)^2 + (y1 - y2)^2
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
        minHeap = []
        for x, y in points:
            dist = x**2 + y**2
            minHeap.append((dist, x, y))
        heapq.heapify(minHeap)
        print(minHeap)
        output = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            output.append([x, y])
            k -= 1
        return output

    # https://leetcode.com/problems/maximum-subarray/description/ - Kadane's Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        maxV, sum = float("-inf"), 0
        for i in range(len(nums)):
            sum += nums[i]
            maxV = max(sum, maxV)
            if sum < 0:
                sum = 0
        return maxV

    # https://leetcode.com/problems/maximum-product-subarray/description/
    def maxProduct(self, nums: List[int]) -> int:
        maxV, prod = float("-inf"), float("-inf")
        for i in range(len(nums)):
            prod *= nums[i]
            maxV = max(prod, maxV)
            if prod < 0:
                prod = 0
        return maxV

    # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
    # if the order is preserved, the mid element should be higher than first, lower than last
    def findMin(self, nums: List[int]) -> int: # must be O(logn)
        def sliced(sublist: list):
            if len(sublist) <= 2:
                return min(sublist)
            median = len(sublist) // 2
            return sliced(sublist[median:]) if sublist[-1] < sublist[median] else sliced(sublist[0:median+1])
        result = sliced(nums)
        return result

    # https://leetcode.com/problems/search-in-rotated-sorted-array/description/
    def searchTarget(self, nums: List[int], target: int) -> int: # 0 log(n). return idx of target or -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    
    # https://leetcode.com/problems/3sum/description/
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        inner_list = [nums[i], nums[j], nums[k]]
                        inner_list.sort()
                        result_set.add(tuple(inner_list))
        
        return list(result_set)

    # https://leetcode.com/problems/container-with-most-water/description/
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                if min(height[i], height[j]) * (j - i) > max_area:
                    max_area = min(height[i], height[j]) * (j - i)
        return max_area


    #######################################################################################################################
    # BINARY
    #######################################################################################################################

    # https://leetcode.com/problems/sum-of-two-integers/
    def getSum(self, a: int, b: int) -> int:
        return int(math.log(math.exp(a) + math.exp(b)))
        #return operator.add(a, b)


    ######################################################################################################################
    # HEAP
    #######################################################################################################################
    
    # https://leetcode.com/problems/merge-k-sorted-lists/description/
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     result = []
    #     result_nodes = []
    #     for node in lists:
    #         result.extend(node)
    #     result.sort()
    #     for i in range(len(result)-1):
    #         current_node = ListNode(result[i], result[i+1]) 
    #         result_nodes.append(current_node)
    #     return result

    # https://leetcode.com/problems/top-k-frequent-elements/description/
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for num in nums:
            occurences[num] = occurences.get(num, 0) + 1     
        # result = sorted(occurences, key=occurences.get, reverse=True)
        result = sorted(occurences, key = lambda x: occurences[x], reverse=True)
        return result[0:k]

        # # https://leetcode.com/problems/find-median-from-data-stream/description/
        # class MedianFinder:

        #     def __init__(self):
        #         self.items = []    

        #     def addNum(self, num: int) -> None:
        #         self.items.append(num)

        #     def findMedian(self) -> float:
        #         median = len(self.items) // 2
        #         return self.items[median] if len(self.items) % 2 else (self.items[median] + self.items[median-1]) / 2
        #         #return float(sum(self.items)) / len(self.items)

    ######################################################################################################################
    # HEAP
    #######################################################################################################################

    # https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
    # Definition for a binary tree node.


# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Binary tree capacity: pow(2, depth)-1
def maxDepth(self, root: Optional[TreeNode]) -> int:
    
    max_depth = 1
    def traverseNode(node):
        nonlocal max_depth
        if node.left:
            max_depth += 1
            traverseNode(node.left)
        if node.right:
            max_depth += 1
            traverseNode(node.right)
    traverseNode(root)
    return max_depth


def main() -> None:
    start = time.time()
    
    # TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}

    null = -100
    # maxDepth(None, [3,9,20,null,null,15,7]) # 3
    # maxDepth(None, [1,null,2]) # 2
    
    print(math.log(1, 2))
    1 2 4 8
    1 3 7 15

    print(f"Done {time.time()-start:.6f}")

if __name__ == "__main__":
    main()



    # print(Solution().twoSum(None, [2,5,5,11], 10)) # [1,2]
    # print(Solution.maxProfit(None, [7,6,4,3,1])) # 0
    # print(Solution.containsDuplicate(None, np.random.randint(0, 10000, 100)))
    # print(Solution.productExceptSelf(None, [1,2,3,4])) # [24, 12, 8, 6]
    # print(Solution.maxSubArray(None, [x*random.random() for x in range(9)])) 
    # print(Solution.maxProduct(None, [2,3,-2,4])) # 6
    # print(Solution.findMin(None, [ 7, 8, 1, 2, 3, 4, 5, 6 ])) # 1
    # print(Solution.searchTarget(None, [2,3,4,5,6,7,8,9,1], 9)) # 7
    # print(Solution.threeSum(None, [-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    # print(Solution.maxArea(None, [1,8,6,2,5,4,8,3,7])) # 49 
    
    # print(Solution.getSum(None, 1, 2))
    # print(Solution.mergeKLists(None, [[1,4,5],[1,3,4],[2,6]])) # [1,1,2,3,4,4,5,6]
    # print(Solution.topKFrequent(None, [1,1,1,2,2,3], 2)) # [1,2]