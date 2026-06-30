class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            # calculate width of container rectangle using indexes
            width = right - left

            # calculate height of container by using smaller of 2 heights (since water can spill out)
            height = min(heights[left], heights[right])

            # calculate new proposed rectangle area
            newArea = width * height

            # compare to find largest area
            maxArea = max(maxArea, newArea)

            # move the pointer with the smaller height
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            elif heights[left] == heights[right]:
                # if they are equal just move one pointer (you can choose, either works)
                right -= 1

        return maxArea



