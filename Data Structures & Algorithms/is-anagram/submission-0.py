class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ht = {}
        t_ht = {}

        if len(s) != len(t):
            return False

        for ch in s:
            if ch not in s_ht:
                s_ht[ch] = 1
            else:
                s_ht[ch] = s_ht[ch] + 1

        for ch in t:
            if ch not in t_ht:
                t_ht[ch] = 1
            else:
                t_ht[ch] = t_ht[ch] + 1

        return s_ht == t_ht



        