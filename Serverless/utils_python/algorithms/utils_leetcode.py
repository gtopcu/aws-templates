
# https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions?s=08

from typing import Tuple, List, Dict, Any, Optional
import time
import math
import numpy as np
import heapq
import random
import sys

class Solution:
    
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


def main() -> None:
    start = time.time()
    # print(Solution().twoSum(None, [2,5,5,11], 10)) # [1,2]
    # print(Solution.maxProfit(None, [7,6,4,3,1])) # 0
    # print(Solution.containsDuplicate(None, np.random.randint(0, 10000, 100)))
    # print(Solution.productExceptSelf(None, [1,2,3,4])) # [24, 12, 8, 6]
    # print(Solution.maxSubArray(None, [-2,1,-3,4,-1,2,1,-5,4])) # 6 9/36
    # print(Solution.maxSubArray(None, [x*random.random() for x in range(9)])) 
    print(Solution.maxProduct(None, [2,3,-2,4])) # 6

    
    print(f"Done {time.time()-start:.6f}")

if __name__ == "__main__":
    main()

