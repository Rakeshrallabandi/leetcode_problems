from typing import List

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # Sort each row in-place descending
        for row in nums:
            row.sort(reverse=True)
        
        ans = 0
        # Iterate column by column
        for i in range(len(nums[0])):
            k = -1
            for j in range(len(nums)):
                if i < len(nums[j]):
                    k = max(k, nums[j][i])
            ans += k
        
        return ans
