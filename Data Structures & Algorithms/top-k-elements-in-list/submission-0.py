class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sortedItems = sorted(count.items(), key=lambda item: item[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sortedItems[i][0])

        return result


            