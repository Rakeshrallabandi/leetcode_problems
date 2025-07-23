import heapq


class Solution:
    def halveArray(self, a: List[int]) -> int:
        h = [-x for x in a]  
        heapq.heapify(h)

        s = sum(a)  
        r = 0      
        o = 0       

        while r < s / 2:
            x = -heapq.heappop(h)  
            x /= 2                 
            r += x
            heapq.heappush(h, -x)  
            o += 1

        return o
