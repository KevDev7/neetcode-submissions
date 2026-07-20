class Solution:
    def numDecodings(self, s: str) -> int:
        # memo[index] stores the number of ways to decode
        # the substring beginning at index
        memo: Dict[int, int] = {}

        def dfs(index):
            # Reaching the end means we successfully formed one decoding
            if index == len(s):
                return 1

            # A decoding cannot begin with 0
            if s[index] == "0":
                return 0

            if index in memo:
                return memo[index]

            # Choice 1: decode the current character by itself
            ways = dfs(index + 1)

            # Choice 2: decode the current and next characters together
            if (
                index + 1 < len(s)
                and 10 <= int(s[index:index + 2]) <= 26
            ):
                ways += dfs(index + 2)

            memo[index] = ways
            return ways

        return dfs(0)