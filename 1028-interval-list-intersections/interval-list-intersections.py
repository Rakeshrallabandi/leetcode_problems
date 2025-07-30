from typing import List

class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []

        while i < len(first) and j < len(second):
            a_start, a_end = first[i]
            b_start, b_end = second[j]

           
            start = max(a_start, b_start)
            end = min(a_end, b_end)

            if start <= end:
                result.append([start, end])

           
            if a_end < b_end:
                i += 1
            else:
                j += 1

        return result
