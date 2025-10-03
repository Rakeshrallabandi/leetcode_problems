class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=abs, reverse=True)
        
        sum_val = 0
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
            sum_val += nums[i]
        
        if k % 2 == 1:
            sum_val -= 2 * abs(nums[-1])
        
        return sum_val