class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high, low = 0, len(nums) - 1
        while high <= low:
            Mid = high + (low - high) // 2
            if nums[Mid] == target:
                return Mid
            elif nums[Mid] > target:
                low = Mid - 1
            else:
                high = Mid + 1
            if high> low:
                return high 