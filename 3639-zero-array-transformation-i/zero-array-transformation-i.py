class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        p=[0]*len(nums)
        for i,j in queries:
            print(0)
            if j==len(nums)-1:
                p[i]+=1
                
            else:
                p[i]+=1
                p[j+1]-=1
        print(p)
        for i in range(1,len(p)):
            p[i]=p[i]+p[i-1]
        c=0
        for i in range(len(p)):
            if nums[i]-p[i]<=0:
                c+=1
        return c==len(nums)
