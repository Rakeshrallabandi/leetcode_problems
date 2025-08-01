class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        a, b, c = len(s1), len(s2), len(s3)
        if s1 == s2 == s3:
            return 0
        i = 0
        while i < min(a, b, c) and s1[i] == s2[i] == s3[i]:
            i += 1
        if i == 0:
            return -1
        return (a - i) + (b - i) + (c - i)
