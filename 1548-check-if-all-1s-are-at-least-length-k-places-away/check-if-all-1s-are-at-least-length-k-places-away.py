from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == 1:
                break
        else:
            return True  # no 1 found at all

        m = i
        for j in range(i + 1, len(nums)):
            if nums[j] == 1:
                if j - m - 1 < k:
                    return False
                m = j
        return True
