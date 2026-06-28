class Solution:

    def encode(self, strs: List[str]) -> str:
        # Hello World -> 5#Hello5#World
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedList = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            strLength = int(s[i:j])
            decodedStr = s[j + 1 : j + 1 + strLength]
            decodedList.append(decodedStr)
            i = j + strLength + 1

        return decodedList

