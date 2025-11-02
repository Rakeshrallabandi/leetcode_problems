class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        m=sorted(nums, key=lambda x:abs(x))
        i,j=0,len(m)-1
        ans=0
        while i<j:
            ans+=-m[i]*m[i]+m[j]*m[j]
            i+=1
            j-=1
        if len(m)%2==1:
            ans+=m[i]*m[i]
        return ans