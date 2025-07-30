from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = max(nums)
        longest = 0
        count = 0

        for num in nums:
            if num == max_and:
                count += 1
                longest = max(longest, count)
            else:
                count = 0

        return longest
