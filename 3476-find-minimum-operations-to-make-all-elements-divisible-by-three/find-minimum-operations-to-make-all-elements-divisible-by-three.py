class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            if (i+1)%3==0 or (i-1)%3==0:
                ans+=1
            elif (i+2)%3==0 or (i+2)%3==0:
                ans+=2
        return ans
