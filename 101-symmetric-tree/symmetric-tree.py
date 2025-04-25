# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sym(self,p,q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        return q.val==p.val and self.sym(p.left,q.right) and self.sym(q.right,p.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.sym(root,root)