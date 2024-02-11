from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        result = len(nums)
        
        for i , num in enumerate(nums):
            print("Missing",i,num)
            result ^= i ^ num
            print("Missing",result)
            
            
        return result
    
int = Solution()  
nums = [0,1,3,]    
res = int.missingNumber(nums)
print (res)
# time = O(n)        
# space = O(1)        