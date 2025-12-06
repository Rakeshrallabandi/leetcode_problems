class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
          
        num = sorted(list(set(nums)))

        from collections import Counter
        freq = Counter(nums)

        
        num = sorted(num, reverse=True)

        running_greater = 0
        ans = 0

        for v in num:
          
            if running_greater >= k:
                ans += freq[v]

          
            running_greater += freq[v]

        return ans

