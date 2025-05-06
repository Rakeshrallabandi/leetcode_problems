from collections import deque

class Solution(object):
    def level(self, root):
        if not root:
            return []

        d = deque([root])
        result = []

        while d:
            level_size = len(d)
            cur = []

            for _ in range(level_size):
                temp = d.popleft()
                cur.append(temp.val)  # ✅ Append the value, not the node

                if temp.left:
                    d.append(temp.left)
                if temp.right:
                    d.append(temp.right)

            result.append(cur)

        return result

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        return self.level(root)
