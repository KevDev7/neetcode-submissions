class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            counter = 1
            i = n
            while i + 1 in numSet:
                i += 1
                counter += 1
            longest = max(longest, counter)

        return longest
        

