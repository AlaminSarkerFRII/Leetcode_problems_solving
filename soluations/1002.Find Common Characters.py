import math
import string
from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
       
       result = []
       commonCount = [math.inf] * 26
       
       for a in A:
           count = [0] * 26
           
           for c in a:
               count[ ord(c) - ord('a')] += 1
               
           for i in range(26):  
               commonCount[i] = min(commonCount[i], count[i])
               
       for c in string.ascii_lowercase:
            for j in range(commonCount[ord(c) - ord('a')]):
                result.append(c)
                   
       return result
                
       

inst = Solution()
words = ["bella","label","roller"]



print(inst.commonChars(words))

# Expected Output: ["e","l","l"]