class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            curr_interval = intervals[i]

            # case 1: [newInterval, curr_interval] - new interval ends before current interval starts
            # finished mapping out where new interval located, append new interval to end of result and then return result with remaining of intervals
            if newInterval[1] < curr_interval[0]:
                result.append(newInterval)
                return result + intervals[i:]
            # case 2: [curr_interval, newInterval] - new interval starts after current interval ends
            # append current interval to result
            elif curr_interval[1] < newInterval[0]:
                result.append(curr_interval)
            # case 3: new interval overlaps with current interval
            # combine them to make singular bigger interval, let for loop keep running in case inew interval merges with more old intervals
            else:
                newInterval = (
                    min(newInterval[0], curr_interval[0]),
                    max(newInterval[1], curr_interval[1])
                )
        
        # if reach end of for loop, case 1 did not happen
        # so new merged/unmerged interval must be at the very end of all intervals
        result.append(newInterval)

        return result
