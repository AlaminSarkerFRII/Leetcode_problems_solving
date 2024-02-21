from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        availabe = [i for i in range(n)]
        used = []
        count = [0] * n

        for start, end in meetings:
            
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(availabe, room)
                
            if not availabe:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(availabe, room)
                
            room = heapq.heappop(availabe)
            heapq.heappush(used, (end, room))
            count[room] += 1
            
        return count.index(max(count))
    
ints = Solution()

n = 2 
meetings = [[0,10],[1,5],[2,7],[3,4]]

print(ints.mostBooked(n,meetings))