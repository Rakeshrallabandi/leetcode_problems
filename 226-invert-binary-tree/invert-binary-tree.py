# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def call(root):
            if root==None:
                return 
            # if root.left ==None or root.right==None:
            #     return
            root.left,root.right=root.right,root.left
            call(root.right)
            call(root.left)
        call(root)
        return root