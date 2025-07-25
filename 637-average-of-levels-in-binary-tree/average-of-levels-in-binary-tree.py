# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        k=defaultdict(list)
        def call(root,val):
            if root==None:
                return 
            k[val].append(root.val)
            call(root.left,val+1)
            call(root.right,val+1)
            # return 
        call(root,0)
        ans=[]
        print(k)
        for i in k:
            ans.append(sum(k[i])/len(k[i]))
        return ans