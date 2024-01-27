import functools

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        KMOD = 10**9 + 7
        
        @functools.lru_cache(None)
        
        def dp(k:int, i:int, j:int) -> int:
          #Return the number of paths to move the ball  at (i,j) out of bounds with k moves.
          
          if i < 0 or i == m or j < 0 or j == n:
                return 1
          if k == 0:
                return 0
          
          return (dp(k-1, i+1,j)+dp(k-1, i-1, j) + 
                  dp(k-1, i, j+1) + dp(k-1,i,j-1)) % KMOD
          
        return dp(maxMove, startRow, startColumn) 
            
            
            
ins = Solution()

m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0

res = ins.findPaths(m, n, maxMove, startRow, startColumn)

print(res)  