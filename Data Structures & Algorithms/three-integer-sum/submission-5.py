class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # sort nums in asc order
        
        # i = i, j = left, k = right
        for i in range(len(nums)):
            # use the earliest i if dups exist, skip future dups of i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # assign left & right based on i
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # check i + j + k sum 
                threeSum = nums[i] + nums[left] + nums[right]

                # approved sum
                if threeSum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # move left till no more dups
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # move right till no more dups
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward to next distinct num after skipping past dups
                    left += 1
                    right -= 1

                # smaller than 0, move left pointer up 1 to get larger number for sum
                elif threeSum < 0:
                    left += 1

                # larger than 0, move right pointer down 1 to get smaller number for sum
                elif threeSum > 0: 
                    right -= 1
                    
        return result


        