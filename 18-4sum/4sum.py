class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        ans=[]
        dect={}
        for i in range(n):
            for j in range(i+1,n):
                k=j+1
                l=n-1
                
                while k<l:
                    # print(ans)
                    temp=nums[k]+nums[l]+nums[i]+nums[j]
                    if i!=j!=k!=l and temp==target:
                        v=[nums[i],nums[j],nums[k],nums[l]]
                        
                        v.sort()
                        v=tuple(v)
                        if v not in dect:
                            ans.append(v)
                            dect[v]=1
                        k+=1
                        l-=1
                    elif temp<target:
                        k+=1
                    else:
                        l-=1
        return ans
