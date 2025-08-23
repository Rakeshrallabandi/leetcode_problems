import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[-i for i in nums]
        heapq.heapify(heap)
        ans=0
        for i in range(k):
            ans=-heapq.heappop(heap)
        return ans
        
