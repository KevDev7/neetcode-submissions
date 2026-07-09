class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        n = len(self.nums)
        mid = n // 2

        if n % 2 == 1:
            return self.nums[mid]

        return (self.nums[mid - 1] + self.nums[mid]) / 2
        
        