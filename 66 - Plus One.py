class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s=''
        for i in digits:
            s+= str(i)
        res =[]
        s = str(int(s)+1)
        for i in str(s):
            res.append(int(i))
        
        return res