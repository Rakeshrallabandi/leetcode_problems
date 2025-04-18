from collections import deque
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=deque([])
        currentSum=0
        ans=-float('inf')
        n=len(nums)
        for i in range(n):
            if currentSum<0:
                while d and currentSum<0:
                    k=d.popleft()
                    currentSum-=k
            d.append(nums[i])
            currentSum+=nums[i]
            ans=max(ans,currentSum)
        return ans