class Solution:
    def climbStairs(self, n: int) -> int:
        # Start calculating at stair 2 because finding the number of ways to reach a stair requires the known answers for the previous two stairs.
        ways_two_stairs_back = 1  # two steps back from 2 = 0: 1 way (being do nothing)
        ways_one_stair_back = 1   # one stair back from 2 = 1: 1 way (being take one 1 step)

        # Calculate the answers for stairs 2 through n
        for _ in range(n - 1):
            # Add the ways from one stair below and two stairs below
            ways_current_stair = ways_one_stair_back + ways_two_stairs_back

            # Move both saved answers forward one stair
            ways_two_stairs_back = ways_one_stair_back
            ways_one_stair_back = ways_current_stair

        # We return ways_one_stair_back because after the final shift, it contains the answer that was stored in ways_current_stair.
        return ways_one_stair_back