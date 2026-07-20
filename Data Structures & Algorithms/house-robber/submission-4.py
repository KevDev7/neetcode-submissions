class Solution:
    def rob(self, nums: List[int]) -> int:
        # Before checking houses, start at 0
        best_two_houses_back = 0
        best_one_house_back = 0

        # go through each house
        for current_house in nums:
            # option 1: rob house and keep best money from two houses back
            rob_current_house = current_house + best_two_houses_back

            # option 2: skip current house as best money one house back
            skip_current_house = best_one_house_back

            # decide whether option 1 or 2 gives more money
            best_current_house = max(rob_current_house, skip_current_house)

            # increment best_two_houses_back and best_one_house_back forwards by 1
            best_two_houses_back = best_one_house_back
            best_one_house_back = best_current_house

        # return best_one_house_back as it is equal to best_current_house and outside for loop
        return best_one_house_back