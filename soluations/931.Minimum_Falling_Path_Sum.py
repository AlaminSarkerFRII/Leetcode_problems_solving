import math
from typing import List

class Solution:
  def minFallingPathSum(self, A: List[List[int]]) -> int:

    n = len(A)


    for i in range(1,n):
      for j in range(n):
        mini = math.inf
        print("j - i ",j,i)

        for k in range(max(0, j-1), min(n,j+2)) :
            print('k - ',k)
            mini = min(mini,A[i-1][k])
            
            print('mini',mini)

        A[i][j] += mini

    return min(A[-1])
        

instance = Solution()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
res = instance.minFallingPathSum(matrix)
print(res)