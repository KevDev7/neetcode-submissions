class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = "" # empty string
        for s in strs:
            # Hello World -> 5#Hello5#World
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedList = [] # list to hold each string
        i = 0
        while i < len(s):
            j = i

            # find index of j at "#"
            while s[j] != "#":
                j += 1

            # find int value of string's character length
            strLength = int(s[i:j])

            # decode strng using slicing
            decodedStr = s[j + 1 : j + 1 + strLength]

            # add decoded string to list
            decodedList.append(decodedStr)

            # update i to next starting index for int value of string's character length
            i = j + strLength + 1

        return decodedList

