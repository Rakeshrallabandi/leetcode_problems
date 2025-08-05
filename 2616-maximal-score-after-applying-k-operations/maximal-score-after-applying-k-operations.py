import heapq,math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        l=[-i for i in nums]
        heapq.heapify(l)
        ans=0
        while k:
            p=-heapq.heappop(l)
            heapq.heappush(l,-math.ceil(p/3))
            ans+=p
            k-=1
            
        return ans


