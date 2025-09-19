# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def call(root,maxval):
            if root==None:
                return 0
            good=1 if root.val>=maxval else 0
            maxval=max(root.val,maxval)
            return good+ call(root.left,maxval)+ call(root.right,maxval)
        return call(root,root.val)
        