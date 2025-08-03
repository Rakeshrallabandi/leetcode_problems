class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=min(nums)
        ans=00
        for i in nums:
            ans+=i-m
        return ans
