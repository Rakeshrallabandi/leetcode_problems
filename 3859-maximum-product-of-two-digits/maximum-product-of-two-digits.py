class Solution:
    def maxProduct(self, n: int) -> int:
        n=list(str(n))
        n=list(map(int,n))
        n.sort()

        return n[-1]*n[-2]