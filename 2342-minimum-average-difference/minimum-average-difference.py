class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        k=sum(nums)
        j=len(nums)
        if j==1 or k==0:
            return 0
        p=0
        ind=0
        ans=float('inf')
        for i in range(len(nums)-1):
            p+=nums[i]
            m=abs((p//(i+1))-((k-p)//(j-i-1)))
            print(p,i+1,(k-p),j-i-1)
            print(m)
            if ans>m:
                ans=m
                ind=i
        if k/(j)<ans:
            ind=j-1
        return ind


