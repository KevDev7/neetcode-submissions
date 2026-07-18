class Solution:
    def climbStairs(self, n: int) -> int:
        previous_ways = 1  # Ways to reach stair 0
        current_ways = 1   # Ways to reach stair 1

        for i in range(n - 1):
            next_ways = current_ways + previous_ways

            previous_ways = current_ways
            current_ways = next_ways

        return current_ways