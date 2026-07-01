class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        strSet = set()

        for right in range(len(s)):
            # if right points to dup char, remove left chars until no more dup
            while s[right] in strSet:
                strSet.remove(s[left])
                left += 1
            
            # add new char to set
            strSet.add(s[right])

            longest = max(longest, len(strSet))

            right += 1

        return longest

        