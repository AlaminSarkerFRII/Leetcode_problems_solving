class Solution:
     def isPalindrome(self, x: int) -> bool:
          if x <=0:
               return False
          number = x
          reverse = 0

          while number:
               reverse = reverse * 10 + number % 10
               print('reverse : ', reverse )
               number = number // 10
               print('number : ', number)
               print('reverse number : ', reverse)

          return x == reverse
     
instance = Solution()

res = instance.isPalindrome(121)
print(res)