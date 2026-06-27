class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sd = {}
        td = {}

        for ch in s:
            if ch not in sd:
                sd[ch] = 1
            else:
                sd[ch] = sd[ch] + 1
        
        for ch in t:
            if ch not in td:
                td[ch] = 1
            else:
                td[ch] = td[ch] + 1

        return sd == td
        