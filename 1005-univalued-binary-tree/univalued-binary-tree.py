# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        s=set()
        def f(root):
            if root==None:
                return
            s.add(root.val)
            f(root.left)
            f(root.right)
            return len(s)==1
        return f(root)