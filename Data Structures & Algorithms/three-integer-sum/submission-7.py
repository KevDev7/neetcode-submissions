class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # skip future i dups
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # left = j, right = k
            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # skip left and right dups
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # move left and rigth inwards 1 to get next unique number
                    left += 1
                    right -= 1

                elif three_sum < 0:
                    # get larger sum by moving left up 1
                    left += 1
                elif three_sum > 0:
                    # get smaller sum by moving right back 1
                    right -= 1

        return result
