class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            currArea = width * height
            maxArea = max(maxArea, currArea)

            # the shorter wall determines the height & area so move the pointer of shorter height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea


