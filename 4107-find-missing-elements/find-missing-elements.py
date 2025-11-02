class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m,n=min(nums),max(nums)
        nums=set(nums)
        ans=[]
        for i in range(m,n):
            if i not in nums:
                ans.append(i)
        return ans