class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            # i = index at 1st number of string length
            # j = index at "#"
            j = i

            while s[j] != "#":
                j += 1
            
            # get string length number
            stringLength = int(s[i:j])

            # get string
            string = s[j + 1 : j + 1 + stringLength]

            decoded.append(string)

            i = j + 1 + stringLength
        
        return decoded



            



        return []
