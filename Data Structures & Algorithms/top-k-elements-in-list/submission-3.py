class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        my_dict = {}

        for num in nums:
            if num not in my_dict:
                my_dict[num] = 0

            # increment 1
            my_dict[num] += 1
        
        # sort my dict value desc
        sortedList = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            result.append(sortedList[i][0])

        return result
        

