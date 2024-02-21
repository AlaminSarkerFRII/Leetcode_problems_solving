import bisect


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = bisect.bisect_left(range(num), num,
                               key = lambda m: m * m)
        return l**2 == num


inst = Solution()

n = 16
res = inst.isPerfectSquare(n)
print(res)

