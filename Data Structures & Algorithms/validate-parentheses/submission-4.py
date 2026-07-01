class Solution:
    def isValid(self, s: str) -> bool:

        # keep a dict of closing brackets & their corresponding opening brackets
        closingBrackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        
        for ch in s:
            # opening bracket, add to stack
            if ch not in closingBrackets:
                stack.append(ch)

            # closing bracket, check if it has corresponding opening bracket at top of stack
            else:
                # if stack empty, cannot have corresponding opening bracket
                if not stack:
                    return False

                # get opening bracket on top of stack
                top = stack.pop()

                # opening bracket does not correpond to closing bracket
                if top != closingBrackets[ch]:
                    return False
        
        # if stack not empty, then still remaining opening brackets with no corresponding closing brackets
        return not stack


