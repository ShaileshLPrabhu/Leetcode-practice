class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts= {}

        for i in s:
            if i in counts:
                counts[i] +=1
            else:
                counts[i] = 1
    
        for key,value in counts.items():
            if value ==1:
                return s.index(key)
                break
                
        return -1 