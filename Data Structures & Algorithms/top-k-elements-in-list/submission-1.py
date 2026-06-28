class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []
        countFreq = {}

        for num in nums:
            # count how many times number appears
            # .get(num, 0) - retrieve number of occurence if already exist, else return 0
            countFreq[num] = countFreq.get(num, 0) + 1

        # sort countFreq dict by item's values in descending order
        # sortedItems is a list from sorted(), the list is filled with tuples from .items()
        sortedItems = sorted(countFreq.items(), key = lambda item: item[1], reverse=True)
        
        for i in range(k):
            result.append(sortedItems[i][0])

        return result

        
            
        