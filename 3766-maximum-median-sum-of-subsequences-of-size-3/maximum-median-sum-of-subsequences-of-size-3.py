from collections import deque
class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        k=deque(nums)
        ans=0
        print(k)
        while len(k)!=0:
            k.popleft()
            k.pop()
            ans+=k.pop()
        return ans
        
        