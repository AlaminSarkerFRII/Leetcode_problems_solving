import heapq
from itertools import pairwise
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        minHeap = []
        
        for i,(a,b) in enumerate(pairwise(heights)):
            
            diff = b - a
            
            if diff <=0:
                continue
            heapq.heappush(minHeap,diff)
            if len(minHeap) > ladders:
                bricks -=heapq.heappop(minHeap)
            if bricks < 0:
                return i
        return len(heights) -1

ints = Solution()
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
print(ints.furthestBuilding(heights, bricks, ladders))
            
        