# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def call(root):
        
            if root==None:
                return
            if root.val%2==0:
                if root.left and root.left.left:
                    ans[0]+=root.left.left.val
                    print(root.left.left.val)
                if root.left and root.left.right:
                    ans[0]+=root.left.right.val
                    print(root.left.right.val)
                if root.right and root.right.left:
                    ans[0]+=root.right.left.val
                    print(root.right.left.val)
                if root.right and root.right.right:
                    ans[0]+=root.right.right.val
                    print(root.right.right.val)
            call(root.left)
            
            call(root.right)
        call(root)
        return ans[0]