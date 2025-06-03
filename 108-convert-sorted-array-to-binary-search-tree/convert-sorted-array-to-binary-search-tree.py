# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(n):
            if len(n)==0:
                return None
            mid=len(n)//2
            
            root=TreeNode(n[mid])
            root.left=helper(n[:mid])
            root.right=helper(n[mid+1:])
            return root
       
        return  helper(nums)



