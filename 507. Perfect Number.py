class Solution:
    
    def prm(self,x:int) -> int:
        return (2**(x-1)) * ((2**x)-1)
    
    def checkPerfectNumber(self, num: int) -> bool:
        
        primes = [2,3,5,7,13,17.19,31]

        for i in primes:
            if self.prm(i) == num:
                return True
            
        return False