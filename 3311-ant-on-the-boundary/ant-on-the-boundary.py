class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        p=[nums[0]]
        for i in range(1,len(nums)):
            p.append(p[-1]+nums[i])
        return p.count(0)