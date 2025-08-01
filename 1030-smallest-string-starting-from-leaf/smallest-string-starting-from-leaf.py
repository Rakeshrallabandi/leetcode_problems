class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []

        def dfs(node, path):
            if not node:
                return
            path = chr(node.val + ord('a')) + path
            if not node.left and not node.right:
                ans.append(path)
                return
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, '')
        return min(ans)
