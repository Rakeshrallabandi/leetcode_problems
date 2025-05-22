class Solution(object):
    def modifiedMatrix(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        temp=[-float('inf')]*len(m[0])
        for i in range(len(m)):
            for j in range(len(m[0])):
                temp[j]=max(temp[j],m[i][j])
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j]==-1:
                    m[i][j]=temp[j]
        return m
        