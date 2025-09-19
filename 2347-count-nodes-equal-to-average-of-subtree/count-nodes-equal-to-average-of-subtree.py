class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(u):
            nonlocal cnt
            if not u:
                return (0, 0)
            ls, lc = dfs(u.left)
            rs, rc = dfs(u.right)
            s = ls + rs + u.val
            c = lc + rc + 1
            if u.val == s // c:
                cnt += 1
            return (s, c)
        cnt = 0
        dfs(root)
        return cnt