class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        k=[0]*len(mat[0])
        l=[0]*len(mat)
        m={}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                m[mat[i][j]]=[i,j]
        print(m)
        for p in range(len(arr)):
            
            i,j=m[arr[p]]
            
            k[j]+=1
            l[i]+=1
            if k[j]==len(mat) or l[i]==len(mat[0]):
                return p
        return 0
            