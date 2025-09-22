class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        k={}
        for i in nums:
            k[i]=k.get(i,0)+1
        m=0
        for i in k:
            m=max(m,k[i])
        ans=0
        for i in k:
            if k[i]==m:
                ans+=k[i]
        return ans