class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # skip i dups
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # j = left, k = right
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]

                if threeSum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # skip left & right dups
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # move left and right inwards by 1 to next unique chars
                    left += 1
                    right -= 1

                elif threeSum < 0:
                    # smaller than 0, move left forward to get bigger number
                    left += 1

                elif threeSum > 0:
                    # bigger than 0, move right backwards to get smaller number
                    right -= 1

        return result
