class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            # If char is an opening bracket, save it for later.
            if char not in matching_open:
                stack.append(char)
                continue

            # If char is a closing bracket, there must be a matching
            # opening bracket at the top of the stack.
            if not stack:
                return False

            top = stack.pop()

            if top != matching_open[char]:
                return False

        # Valid only if every opening bracket got closed.
        return len(stack) == 0