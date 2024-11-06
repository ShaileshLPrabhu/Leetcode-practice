class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = ""
        for i in nums:
            s+=str(i)

        digsum =0
        for i in s:
            digsum+= int(i)
        
        return abs(digsum-sum(nums))