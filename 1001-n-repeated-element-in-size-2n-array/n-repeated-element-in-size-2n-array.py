class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        k={}
        for i in nums:
            if i in k:
                k[i]+=1
            else:
                k[i]=1
        for i in k:
            if k[i]==len(nums)//2:
                return i
            