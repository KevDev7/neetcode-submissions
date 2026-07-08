class Solution:
    def isValid(self, s: str) -> bool:
        # python stacks use list
        stack = []
        closing_brackets = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        # loop thru each char in string
        for ch in s:
            # ch is opening brackets, store in stack
            if ch not in closing_brackets:
                stack.append(ch)
            else:
                # done with all opening brackets, ch on closing brackets now

                # if stack empty, no opening brackets for closing brackets
                if not stack:
                    return False

                # get top opening bracket char from stack
                opening_bracket = stack.pop()

                # if closing bracket don't correspond with opening bracket, invalid parenthesis
                if closing_brackets[ch] != opening_bracket:
                    return False
        
        # if remaining stack, invalid pathentheses
        if stack:
            return False
        
        return True



            
            

