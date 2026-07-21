class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removal_counter = 0

        # Sort the intervals using ending value in ascending order as ends earlier leaves more room later
        intervals.sort(key=lambda interval: interval[1])

        # Set 1st interval to previous_interval to compare with later intervals in sorted intervals list 
        prev_interval = intervals[0]

        # Unpack each interval to compare skipping first one (at index 0)
        for curr_start, curr_end in intervals[1:]:
            # current interval start < previous interval end -> overlap found
            if curr_start < prev_interval[1]:
                removal_counter += 1
            # no overlap found, set current interval as previous interval to check in next iteration
            else:
                prev_interval = [curr_start, curr_end]

        return removal_counter

        