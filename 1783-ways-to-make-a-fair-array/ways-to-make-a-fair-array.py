from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even = [0]   # prefix sum of even indices
        odd = [0]    # prefix sum of odd indices
        c = 0

        # Build prefix sums
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(even[-1] + nums[i])
                odd.append(odd[-1])
            else:
                odd.append(odd[-1] + nums[i])
                even.append(even[-1])

        n = len(nums)
        for i in range(len(nums)):
            
            even_sum = even[i] + (odd[n] - odd[i+1])
            
            odd_sum = odd[i] + (even[n] - even[i+1])
            if even_sum == odd_sum:
                c += 1

        return c
