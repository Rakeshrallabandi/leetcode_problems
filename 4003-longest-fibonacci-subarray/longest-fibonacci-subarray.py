class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=2
        a=2
        for i in range(2,len(nums)):
            
            if nums[i]==nums[i-1]+nums[i-2]:
                ans+=1
                a=max(ans,a)
            else:
                
                ans=2
        return a
