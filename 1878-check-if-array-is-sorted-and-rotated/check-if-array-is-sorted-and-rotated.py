class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                c+=1
        if nums[-1]>nums[0]:
            c+=1
        return True if c==1 or c==0 else False