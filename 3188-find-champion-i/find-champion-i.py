class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        ans=0
        j=0
        for i in range(len(grid)):
            c=grid[i].count(1)
            if ans<c:
                j=i
                ans=c
        return j