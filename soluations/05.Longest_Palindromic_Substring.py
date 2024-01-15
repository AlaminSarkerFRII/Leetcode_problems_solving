class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""      # To store the result (longest palindrome)
        resLen = 0     # To store the length of the longest palindrome

        for i in range(len(s)):
            # Check for odd length palindromes
            l, r = i, i   # Initialize the pointers to the current character
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]  # Update the result if a longer palindrome is found
                    resLen = r - l + 1
                l -= 1
                r += 1
                print(resLen)
                print(res)

            # Check for even length palindromes
            l, r = i, i + 1  # Initialize the pointers to the current character and the next one
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]  # Update the result if a longer palindrome is found
                    resLen = r - l + 1
                l -= 1
                r += 1
                print(resLen)
                print(res)

        return res


instance = Solution()
res = instance.longestPalindrome("aabaa")
print (res)

