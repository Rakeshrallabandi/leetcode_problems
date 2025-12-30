class Solution:
    def mirrorDistance(self, n: int) -> int:
        k=str(n)[::-1]
        return abs(int(k)-n)