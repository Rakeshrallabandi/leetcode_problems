class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums.sort()
        ans = []
        start = ''
        
        for i in range(len(nums)):
            if len(start) == 0:
                start = str(nums[i])
            
            
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == str(nums[i]) or len(start)==0:
                    ans.append(str(nums[i]))
                else:
                    ans.append(str(start) + "->" + str(nums[i]))
                
                start = ''  
        
        return ans