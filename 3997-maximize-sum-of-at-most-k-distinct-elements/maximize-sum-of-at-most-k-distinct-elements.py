class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums=list(set(nums))
        nums.sort(reverse=True)
        if len(nums)<k:
            return nums
        return nums[:k]