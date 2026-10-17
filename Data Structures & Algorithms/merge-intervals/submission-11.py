class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort()
        
        new_intervals = []

        new_intervals.append(intervals[0])

        for i in range(1, len(intervals)):

            if new_intervals[-1][1] >= intervals[i][0]:

                new_intervals[-1][0] = min(new_intervals[-1][0], intervals[i][0])
                new_intervals[-1][1] = max(new_intervals[-1][1], intervals[i][1])
            
            else:
                new_intervals.append(intervals[i])
        
        return new_intervals