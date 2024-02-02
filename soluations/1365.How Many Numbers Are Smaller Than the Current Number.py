from typing import List
import collections


class Solution:
    def countSmallerThanCurrentNumber(self, nums : List[int])-> List[int]:
        count = collections.Counter(nums)
        kMax = 100
        
        for i in range(1, kMax+1):
            count[i] +=count[i-1]
            print(count)
        return [0 if num == 0 else count[num -1] 
                for num in nums 
                ]
ins  = Solution()

nums = [8,1,2,2,3]
res = ins.countSmallerThanCurrentNumber(nums)

print(res)

"""
Js code

----
class Solution {
    countSmallerThanCurrentNumber(nums) {
        const count = Array(101).fill(0); // Assuming the range of numbers is [0, 100]

        nums.forEach(num => {
            count[num]++;
        });

        const result = nums.map(num => count.slice(0, num).reduce((acc, val) => acc + val, 0));
        return result;
    }
}

// Example usage:
const solution = new Solution();
const nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
console.log(solution.countSmallerThanCurrentNumber(nums));




"""

