from collections import defaultdict
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)
        
        for row in matrix:
            
            key = tuple([x ^ row[0] for x in row])
            count[key] += 1
        
        return max(count.values())
