import heapq

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapq.heapify(heap)
        score = 0
        while len(heap) > 1:
            score += 1
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            x -= 1
            y -= 1
            if x > 0:
                heapq.heappush(heap, -x)
            if y > 0:
                heapq.heappush(heap, -y)
        return score
