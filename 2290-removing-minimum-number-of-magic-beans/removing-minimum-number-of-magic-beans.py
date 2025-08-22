class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        ans = float('inf')
        
        n = len(beans)
        for i in range(n):
           
            removed = total - beans[i] * (n - i)
            ans = min(ans, removed)
        return ans
