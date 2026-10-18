class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        count = 0
        i = 1
        prevend = intervals[0][1]
        while i < len(intervals):
            if intervals[i][0] < prevend:

                prevend = min(intervals[i][1], prevend)
                count += 1
                i += 1

            else:
                prevend = intervals[i][1]
                i += 1

        
        return count
        



        