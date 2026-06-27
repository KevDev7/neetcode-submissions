class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            charCount = [0] * 26

            for ch in s:
                charCount[ord(ch) - ord("a")] += 1

            key = tuple(charCount)

            if key not in result:
                result[key] = []

            result[key].append(s)

        return list(result.values())

            