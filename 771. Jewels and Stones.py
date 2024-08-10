class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels = list(jewels)
        stones = list(stones)
        counter=0
        for i in stones:    
            if i in jewels:
                 counter+=1 
        return counter
    
s=Solution()
print(s.numJewelsInStones("aA","aAAbbbb")) #jewels = "aA", stones = "aAAbbbb"