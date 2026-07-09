class MedianFinder:

    def __init__(self):
        # create heaps using list
        # self. because these instance variables will be used across multiple methods in MedianFinder object
        self.small_half = [] # small_half = max heap (use negative), since median is largest of small half
        self.large_half = [] # large_half - min heap, since median is smallest of large half

    def addNum(self, num: int) -> None:
        # first add to small_half max heap using negative value
        heapq.heappush(self.small_half, -num)

        # move num around if following cases:

        # peek to see if largest num in small_half is greater than smallest num in large_half, move num to large_half
        if self.small_half and self.large_half and -self.small_half[0] > self.large_half[0]:
            value = -heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, value)

        # if small_half size greater than large_half by more than 1, move num around so diff in size between the two is <= 1
        if len(self.small_half) > len(self.large_half) + 1:
            value = -heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, value)
        # if large_half size greater than small_half by more than 1, move num around so diff in size between the two is <= 1
        elif len(self.large_half) > len(self.small_half) + 1:
            value = heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, -value)

    def findMedian(self) -> float:
        # if size of small_half greater than size of large_half, small_half contains median
        if len(self.small_half) > len(self.large_half):
            return -self.small_half[0]
        # if size of large_half greater than size of small_half, large_half contains median
        elif len(self.large_half) > len(self.small_half):
            return self.large_half[0]

        # length of small_half and large_half equal, so calculate mean
        return (-self.small_half[0] + self.large_half[0]) / 2
        
        