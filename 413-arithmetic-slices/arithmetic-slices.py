class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # d=None
        # c=0
        # ans=0
        # j=0
        # while j!=len(nums)-1:
        #     if d==None:
        #         d=nums[j+1]-nums[j]
        #         c+=1
        #     elif nums[j+1]-nums[j]==d:
        #         c+=1
        #     else:
        #         ans+=max(c+1-3,0)
        #         c=0
        #         d=None
        #     print(c,d,j)
        #     j+=1
        # ans+=max(c+1-3,0)
        # return ans
        ans=0
        for i in range(len(nums)):
            d=None
            c=0
            for j in range(i,len(nums)-1):
                if d==None:
                    d=nums[j+1]-nums[j]
                    c+=1
                elif nums[j+1]-nums[j]==d:
                    c+=1
                else:
                    break
            
            if c>1:
                ans+=max(c-1,0)
        return ans