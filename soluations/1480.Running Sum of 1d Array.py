
import itertools
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # method - 01
        # return itertools.accumulate(nums)
        # method - 02
        # reduced memory size --
        result = []
        current_sum = 0
        for num in nums:
            current_sum += num
            result.append(current_sum)
        return result

        

inst = Solution()
nums = [1, 1, 2, 5, 6, 7]
res = inst.runningSum(nums)

print(res)