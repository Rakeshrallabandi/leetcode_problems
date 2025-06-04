class Solution:
    def titleToNumber(self, c: str) -> int:
        ans = 0
        for ch in c:
            ans = ans * 26 + (ord(ch) - ord('A') + 1)
        return ans
