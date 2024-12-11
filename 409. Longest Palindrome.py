class Solution:
    def longestPalindrome(self, s: str) -> int:
        dct = {}
        for i in s:
            if i not in dct:
                dct[i]=1
            else:
                dct[i]+=1

        out=0
        flag_odd = False
        for i in dct:
            if dct[i]%2==0:
                out+=dct[i]
            else:
                out+=dct[i]-1
                flag_odd = True
            
        return out+1 if flag_odd else out
        
        