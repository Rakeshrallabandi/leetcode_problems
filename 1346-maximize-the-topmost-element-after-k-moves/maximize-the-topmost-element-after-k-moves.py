class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums)==1 and k%2==1:
            return -1
        elif len(nums)==1 and k%2==0:
            return nums[0]
        elif k==1:
            return nums[1]
        elif k==0:
            return nums[0]
        elif len(nums)<k:
            return max(nums)
        else:
            p=nums[:k-1]
            ans=max(p)
            if k<len(nums):
                ans=max(ans,nums[k])
            return ans