class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        sm = 0
        c=0
        for i in range(1,n+1):
            if i in banned:
                continue
            sm+= i 
            if sm > maxSum:
                break
            c+=1
        return c


                    
                