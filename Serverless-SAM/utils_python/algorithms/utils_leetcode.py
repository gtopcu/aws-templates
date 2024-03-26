
# https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions?s=08

from typing import Tuple, List, Dict, Any, Optional
import pytest
import time
import numpy as np

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
        output = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                output[i] *= nums[j]
        return output


def main() -> None:
    start = time.time()
    # print(Solution().twoSum(None, [2,5,5,11], 10)) # [1,2]
    # print(Solution.maxProfit(None, [7,6,4,3,1])) # 0
    # print(Solution.containsDuplicate(None, np.random.randint(0, 10000, 100)))
    print(Solution.productExceptSelf(None, [1,2,3,4])) # [24, 12, 8, 6]

    # list = []
    # list[0] = 1
    # list = [None] * len(i)
    # j = [l for l in i]
    # j = i[:]
    # j = list(i)
    # arr = [[]]
    print(f"Done {time.time()-start:.6f}")

if __name__ == "__main__":
    main()

