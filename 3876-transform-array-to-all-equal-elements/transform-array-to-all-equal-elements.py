class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        
        if len(set(nums))==1:
            return True
        #1
        c,c1=0,0
        temp=nums[:]
        for i in range(1,len(nums)):
            if nums[i-1]==-1:
                nums[i]*=-1
                nums[i-1]*=-1
                c+=1
        for i in range(1,len(temp)):
            if temp[i-1]==1:
                temp[i]*=-1
                temp[i-1]*=-1
                c1+=1
        if c1<=k and len(set(temp))==1:
            return True
        if c<=k and len(set(nums))==1:
            return True
        return False
            
        