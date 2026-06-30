class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Move left pointer past duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Move right pointer past duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward
                    left += 1
                    right -= 1

                elif total < 0:
                    # Need a bigger sum, so move left right
                    left += 1

                else:
                    # Need a smaller sum, so move right left
                    right -= 1

        return res

        