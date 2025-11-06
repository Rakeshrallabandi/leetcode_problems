class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        k = 0
        if nums[-1] <= 0:
            return len([x for x in nums if x < 0])
        if nums[0] >= 0:
            return len([x for x in nums if x > 0])
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < 0 and nums[mid + 1] >= 0:
                k = mid
                break
            elif nums[mid] < 0:
                i = mid + 1
            else:
                j = mid
        n = k + 1
        while n < len(nums) and nums[n] == 0:
            n += 1
        return max(k + 1, len(nums) - n)
