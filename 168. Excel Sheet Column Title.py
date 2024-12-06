class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber >0:
            columnNumber-=1
            char = columnNumber%26
            res+= chr(char+ord('A'))
            columnNumber = columnNumber//26
        return res[::-1]