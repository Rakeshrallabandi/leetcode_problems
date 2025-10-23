class Solution:
    def scoreBalance(self, s: str) -> bool:
      
        total = sum(ord(ch) - ord('a') + 1 for ch in s)
        left_sum = 0
        for i in range(1, len(s)):
            left_sum += ord(s[i - 1]) - ord('a') + 1
            if left_sum == total - left_sum:
                return True
        return False
