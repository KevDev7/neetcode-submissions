class Solution:
    def climbStairs(self, n: int) -> int:
        # start with n = 2
        # get known answers for base cases stairs 0 and 1
        ways_two_stairs_back = 1    # two steps back from 2 = 0: 1 way (being do nothing)
        ways_one_stair_back = 1     # one stair back from 2 = 1: 1 way (being take one 1 step)

        for _ in range(n - 1):
            # Reach the next stair from one or two stairs below
            ways_current_stair = ways_one_stair_back + ways_two_stairs_back

            # Move both saved answers forward one stair
            ways_two_stairs_back = ways_one_stair_back
            ways_one_stair_back = ways_current_stair

        # ideally return ways_current_stair but that is stuck in for loop
        # ways_one_stair_back = ways_current_stair so it'll work too
        return ways_one_stair_back
