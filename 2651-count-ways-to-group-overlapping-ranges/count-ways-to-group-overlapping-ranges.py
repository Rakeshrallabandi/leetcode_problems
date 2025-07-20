from typing import List

class Solution:
    def countWays(self, r: List[List[int]]) -> int:
        MOD = 10**9 + 7
        r.sort()
        c = 1
        m = r[0][1]
        for i in range(1, len(r)):
            if r[i][0] > m:
                c += 1
                m = r[i][1]
            else:
                m = max(m, r[i][1])
        return pow(2, c, MOD)

