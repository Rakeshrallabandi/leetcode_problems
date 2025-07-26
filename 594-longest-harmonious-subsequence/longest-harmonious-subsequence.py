class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        p={}
        for i in nums:
            if i in p:
                p[i]+=1
            else:
                p[i]=1
        k=[i for i in p]
        ans=0
        for i in range(1,len(k)):
            if k[i]-k[i-1]==1:
                ans=max(ans,p[k[i]]+p[k[i-1]])
        return ans




