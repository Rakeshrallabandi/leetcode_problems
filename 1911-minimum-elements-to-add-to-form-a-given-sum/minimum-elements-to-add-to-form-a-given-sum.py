class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s=sum(nums)
        k=abs(goal-s)
        return k//limit if k%limit==0 else k//limit+1