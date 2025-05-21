class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=matrix
        r=[1]*len(n)
        c=[1]*len(n[0])

        for i in range(len(n)):
            for j in range(len(n[0])):
                if n[i][j]==0:
                    r[i]=0
                    c[j]=0
        for i in range(len(n)):
            for j in range(len(n[0])):
                if r[i]==0 or c[j]==0:
                    n[i][j]=0
        return n
            