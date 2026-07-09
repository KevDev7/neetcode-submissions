import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap using negative numbers
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # Add to small first
        heapq.heappush(self.small, -num)

        # Make sure every number in small <= every number in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Balance sizes so neither heap is more than 1 bigger
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)
        elif len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        # If small has more numbers, its top is the median
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If large has more numbers, its top is the median
        elif len(self.large) > len(self.small):
            return self.large[0]
        # If equal size, median is average of both middle values
        elif len(self.large) == len(self.small):
            return (-self.small[0] + self.large[0]) / 2
        
        