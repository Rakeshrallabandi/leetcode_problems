import math
from typing import List

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            lcm = nums[i]
            if lcm == k:
                count += 1
            for j in range(i + 1, len(nums)):
                lcm = math.lcm(lcm, nums[j])
                if lcm == k:
                    count += 1
                elif lcm > k:  
                    break
        return count
