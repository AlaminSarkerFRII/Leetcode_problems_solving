from typing import List

class Solution:
  def countOperationsToEmptyArray(self, nums: List[int]) -> int:
      
      n = len(nums)
      result = n
      
      numToIndex = {}
      
      for i , num in enumerate(nums):
          numToIndex[num] = i
          
          
      nums.sort()

      for i in range(1, n):
          
        if numToIndex[nums[i]] < numToIndex[nums[i - 1]]:
              result += n - i
              
      return result
  
ints = Solution()

nums = [3,4,-1]
res = ints.countOperationsToEmptyArray(nums)
print(res) 


"""
reduced run times in this Solution 


--==========


from typing import List

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        max_index = n - 1

        for i in range(n - 1, -1, -1):
            if nums[i] == max_index:
                max_index -= 1
            else:
                result += 1

        return result


"""
