class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1,sum2 = 0,0
        for i in t:
            sum1+=ord(i)

        for i in s:
            sum2+=ord(i)
        
        return chr(sum1-sum2)