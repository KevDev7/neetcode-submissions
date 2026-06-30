class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numSet:
                counter = 1
                while n + counter in numSet:
                    counter += 1
                longest = max(longest, counter)
        return longest