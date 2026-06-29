class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # move to left outermost alphanumerical char
            while left < right and not s[left].isalnum():
                left += 1

            # move to right outermost alphanumerical char
            while left < right and not s[right].isalnum():
                right -= 1

            # check if left outermost and right outermost alphanumerical char lowercase match
            if s[left].lower() != s[right].lower():
                return False

            # increment left index and right index closer to middle
            left += 1
            right -= 1
        
        return True