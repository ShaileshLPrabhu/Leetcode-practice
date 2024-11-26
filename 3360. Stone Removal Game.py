class Solution:
    def check(self,n,x,alice):
        if n < x:
            return alice
        return self.check(n-x,x-1,not alice)

    def canAliceWin(self, n: int) -> bool:
        x = 10
        alice = False
        out = self.check(n,x,alice)
        return out