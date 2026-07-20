class Solution:
    def rob(self, nums: List[int]) -> int:
        # Before checking any houses, the best amount is 0
        best_two_houses_back = 0
        best_one_house_back = 0

        for current_house_money in nums:
            # Choice 1: rob this house and add the best from two houses back
            rob_current_house = current_house_money + best_two_houses_back

            # Choice 2: skip this house and keep the previous best
            skip_current_house = best_one_house_back

            # Save the better of the two choices
            best_current = max(rob_current_house, skip_current_house)

            # Move the saved answers forward one house
            best_two_houses_back = best_one_house_back
            best_one_house_back = best_current

        return best_one_house_back