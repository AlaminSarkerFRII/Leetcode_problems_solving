

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max1 = 0
        max2 = 0
        
        for num in nums:
            if num > max1:
                max2 , max1 = max1, num
            if num > max2:
                max2 = num
      
        return (max1 - 1) * (max2 - 1)