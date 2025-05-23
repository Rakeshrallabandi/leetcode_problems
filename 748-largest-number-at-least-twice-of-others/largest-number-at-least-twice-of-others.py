class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        ans=-1
        for i in range(len(nums)):
            if m==nums[i]:
                ans=i
            else:
                if nums[i]*2<=m:
                    continue
                else:
                    return -1
        return ans
