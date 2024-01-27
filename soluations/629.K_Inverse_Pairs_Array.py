# Time - O(nK)
# space - O(nK)

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # KMod = 10**9 + 7
        KMod = 1_000_000_007
        # dp[i][j] := the number of permutations of numbers 1..i with j inverse pairs
        dp = [[0]*(k+1) for _ in range(n+1)]
        
        #if theres no inverse pairs , the permutations is unique '123 ... i'
        
        for i in range(n+1):
            dp[i][0] = 1
            
        for i in range(1, n+1):
            for j in range(1,k+1):
                
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % KMod
                
                if j-i >=0:
                    dp[i][j] = (dp[i][j] - dp[i-1][j-i] + KMod ) % KMod
                
        return dp[n][k]
        
        
ins = Solution()
n = 3
k = 0
res = ins.kInversePairs(n,k)
print(res)