
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        
        num1_set = set(nums1)
        num2_set = set(nums2)
        
        for num in num1_set.intersection(num2_set):
            
            result.append(num)
                
        return result
    
inst = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]

print(inst.intersection(nums1, nums2))