# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        ans=[]
        def s(root):
            if not root:
                return
            ans.append(root.val)
            s(root.left)
            s(root.right)
            
        s(root)
        ans.sort()
        print(ans)
        return ans[k-1]