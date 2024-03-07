from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        count = [0] * ( n + 1)
        
        for a , b in trust:
            count[a] -=1
            count[b] +=1
            
        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i
                
        return -1        
    
    
    
"""
reducing run time and space 


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_count = [0] * (n + 1)  # Use a list for efficiency
        trusting_count = [0] * (n + 1)  # Track trusted-by count for potential judge

        for a, b in trust:
            trusting_count[a] += 1
            if trusting_count[a] > n - 1:  # Early exit if someone trusts more than n-1 people
                return -1

            if trusted_count[b] != 0 and b != a:  # Avoid redundant checks for the same person
                return -1
            trusted_count[b] += 1

        for i in range(1, n + 1):
            if trusted_count[i] == n - 1:
                return i
        return -1


"""
        