class Solution:
    def fillCups(self, amount: List[int]) -> int:
        total = sum(amount)
        largest = max(amount)
        return max(largest, (total + 1) // 2)