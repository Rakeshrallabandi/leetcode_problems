class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        i=len(matrix[0])-1
        m=len(matrix)
        j=0
       
        while i!=-1 and j!=m:
            print(j,i)
            if matrix[j][i]==target:
                return True
            elif matrix[j][i]>target:
                i-=1
            else:
                j+=1
        return False
