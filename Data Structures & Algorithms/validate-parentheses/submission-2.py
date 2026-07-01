class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:
            # char an opening bracket, save it for later.
            if ch not in matching_open:
                stack.append(ch)
            # char a closing bracket, must be matching opening bracket top of stack
            else: 
                # if stack empty, then no opening bracket correponding to closing bracket
                if len(stack) == 0:
                    return False

                # get opening bracket
                top = stack.pop()

                # check if opening bracket corresponds with closing bracket
                if top != matching_open[ch]:
                    return False

        # Valid only if every opening bracket got closed.
        return len(stack) == 0