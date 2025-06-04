class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def call(node):
            nonlocal ans
            if node is None:
                return
            ans += 1
            call(node.left)
            call(node.right)
        call(root)
        return ans
