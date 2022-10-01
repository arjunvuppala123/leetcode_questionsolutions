class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort() 
        
        q, i, res = [], 0, 0
        for day in range(1, 100001):
            while i < len(events) and events[i][0] == day:
                heappush(q, events[i][1])
                i += 1
                
            while q and q[0] < day:
                heappop(q)
            
            if q: 
                heappop(q)
                res += 1
        return res