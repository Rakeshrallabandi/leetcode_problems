class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def C2(m):
            return m * (m - 1) // 2 if m >= 2 else 0
        
        return (C2(n+2)
                - 3*C2(n - limit + 1)
                + 3*C2(n - 2*limit)
                - C2(n - 3*limit - 1))
