# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def call(root):
            if root==None:
                return 
            ans.append(root.val)
            call(root.left)
            call(root.right)
        call(root)
        ans.sort()
        a=float('inf')
        for i in range(1,len(ans)):
            a=min(a,abs(ans[i]-ans[i-1]))
        return a
            