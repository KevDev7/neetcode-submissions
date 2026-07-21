class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals array using interval starting value in ascending order
        intervals.sort(key=lambda interval: interval[0])

        # Use first interval as first interval in merged intervals array
        merged_intervals_arr = [intervals[0]]

        # Unpackage and loop through each interval, skipping the first one (at index 0)
        for curr_start, curr_end in intervals[1:]:
            # Get the end value of the latest added merged interval
            merged_interval_end = merged_intervals_arr[-1][1]

            # If current interval start <= merged interval end, overlap found, merge them
            if curr_start <= merged_interval_end:
                # when mergin use the larger value between both interval end values
                merged_intervals_arr[-1][1] = max(merged_intervals_arr[-1][1], curr_end)

            # No overlap found, add current interval to result
            else:
                merged_intervals_arr.append([curr_start, curr_end])

        return merged_intervals_arr


