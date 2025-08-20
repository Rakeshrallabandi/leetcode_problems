class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        v=0
        ans=0
        for i in nums:
            if i==0:
                v+=1
            else:
                ans+=(v*(v+1))//2
                v=0
        ans+=(v*(v+1))//2
        return ans