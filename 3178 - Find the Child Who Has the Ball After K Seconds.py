class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
       out = k % (2 * (n - 1))
       return out if out<n else (2 * (n - 1))-out
        