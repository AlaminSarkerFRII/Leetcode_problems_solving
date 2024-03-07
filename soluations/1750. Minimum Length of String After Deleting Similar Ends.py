class Solution:
  def minimumLength(self, s: str) -> int:
      i = 0
      j = len(s) - 1
      
      print(j)
      
      while i < j and s[i] == s[j]:
          c = s[i]
          print(c)
          
          while i<=j and s[i] == c:
              i += 1
          while i<=j and s[j] == c:
              j -= 1
      return j - i + 1

inst = Solution()
s = "cabaabac"
result = inst.minimumLength(s)

print(result)

          