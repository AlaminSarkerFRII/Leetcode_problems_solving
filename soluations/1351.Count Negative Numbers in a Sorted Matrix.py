from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        grid.sort()
        
        result = 0
        
        for row in grid :
            for num in row:
                if num < 0:
                    result += 1
                
        return result
    
    
inst = Solution()
words = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(inst.countNegatives(words))

# Time O(m*n)
# Space O(1)

        
        
        