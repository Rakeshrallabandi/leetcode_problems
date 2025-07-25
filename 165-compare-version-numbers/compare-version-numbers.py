class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1 = list(map(int, v1.split('.')))
        v2 = list(map(int, v2.split('.')))
        n = max(len(v1), len(v2))

        for i in range(n):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            if a < b:
                return -1
            elif a > b:
                return 1
        return 0
