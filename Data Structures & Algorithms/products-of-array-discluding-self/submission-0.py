class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        i = 0
        while i < len(nums):
            j = 0
            product = 1
            while j < len(nums):
                if j != i:
                    product *= nums[j]
                j += 1
            result.append(product)
            i += 1

        return result