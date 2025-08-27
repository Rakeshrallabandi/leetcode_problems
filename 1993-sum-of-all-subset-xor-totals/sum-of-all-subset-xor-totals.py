class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        
        for mask in range(1 << n):     
            xor_val = 0
            for j in range(n):
                if mask & (1 << j):     
                    xor_val ^= nums[j]
            ans += xor_val
        
        return ans
