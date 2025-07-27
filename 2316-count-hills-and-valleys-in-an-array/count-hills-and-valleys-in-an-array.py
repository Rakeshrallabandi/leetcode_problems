class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                a.append(nums[i])
        c = 0
        for i in range(1, len(a) - 1):
            if a[i] > a[i - 1] and a[i] > a[i + 1]:
                c += 1
            elif a[i] < a[i - 1] and a[i] < a[i + 1]:
                c += 1
        return c
