from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row = [0] * len(grid[0])
        col = [0] * len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row[j] = 1
                    col[i] = 1
        if sum(row) == 0 or sum(col) == 0:
            return 0
        i, j = 0, len(row) - 1
        while i <= j:
            if row[i] == 0:
                i += 1
                continue
            if row[j] == 0:
                j -= 1
                continue
            break
        ans = j - i + 1
        i, j = 0, len(col) - 1
        while i <= j:
            if col[i] == 0:
                i += 1
                continue
            if col[j] == 0:
                j -= 1
                continue
            break
        ans *= (j - i + 1)
        return ans
