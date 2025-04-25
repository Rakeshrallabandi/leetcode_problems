# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self,root,s,t):
        if root==None:
            return False
        if root.left is None and root.right is None:
            return s + root.val == t
        return self.path(root.left,s+root.val,t) or self.path(root.right,s+root.val,t)

    def hasPathSum(self, root: Optional[TreeNode], t: int) -> bool:
        return self.path(root,0,t)
        