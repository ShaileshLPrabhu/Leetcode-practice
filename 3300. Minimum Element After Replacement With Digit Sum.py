class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        min_sum =0
        for i in range(len(nums)):
            digit_sum = 0
            num = nums[i]
            while num>0:
                digit_sum+=(num%10)
                num = num//10