class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        p=[0]*(len(nums)+1)
        prifix=0

        for i in range(len(nums)):
            prifix+=p[i]
            c=nums[i]-prifix
            if c<0:
                return False
            if c>0:
                if i+k>len(nums):
                    return False
                p[i+k]-=c
                prifix+=c
        return True
            


