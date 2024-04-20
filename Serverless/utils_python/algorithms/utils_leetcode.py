
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
    # Tree
    #######################################################################################################################

    # https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    # # Binary tree capacity: pow(2, depth)-1
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0
    #     if root.left is None and root.right is None:
    #         return 1
    #     max_depth = 1
    #     current_depth = 1
    #     def traverseNode(node):
    #         nonlocal max_depth
    #         nonlocal current_depth
    #         if (node.left is not None):
    #             current_depth += 1
    #             if current_depth > max_depth:
    #                 max_depth = current_depth
    #             traverseNode(node.left)
    #             current_depth -= 1
    #         if (node.right is not None):
    #             current_depth += 1
    #             if current_depth > max_depth:
    #                 max_depth = current_depth
    #             traverseNode(node.right)
    #             current_depth -= 1
    #     traverseNode(root)
    #     return max_depth

    ######################################################################################################################
    # String
    #######################################################################################################################

    # https://leetcode.com/problems/longest-substring-without-repeating-characters/
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        current = []
        for i in s:
            if i in current:
                current = [i]
            else:
                current.extend(i)
                if (len(current) > len(longest)):
                    longest = "".join(current)
        return longest

    # https://leetcode.com/problems/longest-repeating-character-replacement/description/
    def characterReplacement(self, s: str, k: int) -> int:
        longest = ""
        for i in range(0, len(s)):
            if i==0 and k>0 and i < len(s)-2 and s[i+1] == s[i+2]:
                current = [s[i+1]]
                replace_left = k-1
            else:
                current = [s[i]]
                replace_left = k
            for j in range(i+1, len(s)):
                if s[j] == current[-1]:
                    current.extend(current[-1])
                    if len(current) > len(longest):
                        longest = "".join(current)
                else:
                    if replace_left > 0:
                        replace_left -= 1
                        current.extend(current[-1])
                        if len(current) > len(longest):
                            longest = "".join(current)
                    else:
                        current = [s[j]]
                        replace_left = k
        return longest

    # https://leetcode.com/problems/minimum-window-substring/
    def minWindow(self, s: str, t: str) -> str:
        window = ""
        if len(t) > len(s):
            return window
        if s == t:
            return s
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                includes = True
                for k in t:
                    if k not in s[i:j+1]:
                        includes = False
                        break
                if includes:
                    if len(s[i:j+1]) < len(window) or window == "":
                        window = s[i:j+1]
        return window
    
    ######################################################################################################################
    # DynamicProgramming
    #######################################################################################################################
    
    # https://leetcode.com/problems/climbing-stairs/
    def climbStairs(self, n: int) -> int:
        step_map = { 1: 1, 2: 2 }
        def climb(steps: int):
            result = step_map.get(steps)
            if result:
                return result
            else:
                prev1 = climb(steps-1)
                step_map[steps-1] = prev1
                prev2 = climb(steps-2)
                step_map[steps-2] = prev2
                return prev1 + prev2
        return climb(n)

    # https://leetcode.com/problems/coin-change/description/
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        coins.sort()
        def findAmount(coins):
            if len(coins) == 1:
                if coins[0] == amount:
                    return 1
                elif amount % coins[0] == 0:
                    return amount // coins[0]
                else:
                    return -1
            
        
        return findAmount(coins)


def main() -> None:
    start = time.time()

    # print(Solution.climbStairs(None, 4)) # 1-1, 2-2, 3-3, 4-5
    print(Solution.coinChange(None, [], 10)) # 
     
    
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
    # root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
    # root = TreeNode(1, TreeNode(2, TreeNode(4, None, None)), TreeNode(3, None, TreeNode(5, None, None)))
    # print(Solution.maxDepth(None, root)) # 3
    # print(Solution.characterReplacement(None, "ABBB", 2)) # 
    # print(Solution.minWindow(None, "ADOBECODEBANC", "ABC")) # "BANC"
    # print(Solution.minWindow(None, "ab", "a")) # "a"