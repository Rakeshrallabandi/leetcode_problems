import heapq
from collections import defaultdict, deque

class Solution(object):
    def clearStars(self, s):
        n = len(s)
        pq = []  
        m = defaultdict(deque)  
        keep = [True] * n 
        for i in range(n):
            if s[i] == '*':
                smallest = heapq.heappop(pq)  
                idx = m[smallest].pop()     
                keep[i] = False              
                keep[idx] = False           
            else:
                heapq.heappush(pq, s[i])
                m[s[i]].append(i)

        # Build result from characters not marked for removal
        return ''.join(s[i] for i in range(n) if keep[i])