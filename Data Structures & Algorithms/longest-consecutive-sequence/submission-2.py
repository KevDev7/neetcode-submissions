class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence, by checking is does NOT have number 1 below it
            if (n - 1) not in numSet:
                length = 1
                # count length of sequence
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
