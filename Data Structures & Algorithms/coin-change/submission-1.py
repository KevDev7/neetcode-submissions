class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # index = amount of money
        # value = min num of coins to reach amount
        # Create one entry for every amount from 0 through the target amount.
        # Fill each entry with amount + 1 as an impossibly large placeholder.
        min_coins = [amount + 1] * (amount + 1)

        # Base Case: min coins to reach amount 0 will always be 0
        min_coins[0] = 0

        # Loop through every amount from smallest to largest: 1 - amount
        for curr_amount in range(1, amount + 1):
            # Try out every coin
            for coin in coins:
                # make sure coin can actually fit in current amount
                if coin <= curr_amount:
                    # get remaining amount if coin used as last coin to get amount
                    leftover_amount = curr_amount - coin

                    # see which takes fewer coins to reach amount between:
                    # 1: previously found min coins needed to reach amount
                    # 2: 1 (being the 1 coin we used) + fewest num of coins needed to reach leftover amount
                    min_coins[curr_amount] = min(
                        min_coins[curr_amount],
                        1 + min_coins[leftover_amount]
                    )
        # if min_coins[amount] still equals the impossibly large placeholder then no coin combo found that reaches amount
        if min_coins[amount] == amount + 1:
            return -1

        return min_coins[amount]
