class Solution(object):
    def canPartitionGrid(self, grid):
        row = []
        for i in range(len(grid)):
            s = 0
            for j in range(len(grid[0])):
                s += grid[i][j]
            row.append(s)

        r = [0]
        for i in range(len(row)):
            r.append(row[i] + r[-1])

        for i in range(1, len(r)):
            if r[-1] - r[i] == r[i]:
                return True

        co = []
        for i in range(len(grid[0])):
            s = 0
            for j in range(len(grid)):
                s += grid[j][i]
            co.append(s)

        c = [0]
        for i in range(len(co)):
            c.append(co[i] + c[-1])

        for i in range(1, len(c)):
            if c[-1] - c[i] == c[i]:
                return True

        return False
