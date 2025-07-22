from collections import deque, defaultdict
from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = defaultdict(int)      # to count occurrences of elements
        k = deque()               # sliding window
        ans = 0                   # maximum sum of unique subarray
        c = 0                     # current sum

        for i in nums:
            if i not in s:
                s[i] += 1
                k.append(i)
                c += i
            else:
                ans = max(ans, c)
                while k and k[0] != i:
                    front = k.popleft()
                    s[front] -= 1
                    if s[front] == 0:
                        del s[front]
                    c -= front
                
                if k:
                    front = k.popleft()
                    s[front] -= 1
                    if s[front] == 0:
                        del s[front]
                    c -= front
                
                s[i] += 1
                k.append(i)
                c += i

        ans = max(ans, c)
        return ans
