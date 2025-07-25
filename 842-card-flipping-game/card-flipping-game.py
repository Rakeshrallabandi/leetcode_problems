class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                ans.add(fronts[i])
        res = float('inf')
        for x in fronts + backs:
            if x not in ans:
                res = min(res, x)
        return res if res != float('inf') else 0
