class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = 1
        ends = [intervals[0][1]]
        for i in range(1,len(intervals)):
            if intervals[i][0] < min(ends):
                res += 1
            else:
                ends.remove(min(ends))
            ends.append(intervals[i][1])
        return res