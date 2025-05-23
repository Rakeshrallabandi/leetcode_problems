class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k=0
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]%2==0:
                # nums[k],nums[i]=nums[i],nums[i]
                i+=1
            else:
                
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
           
            
        return nums
