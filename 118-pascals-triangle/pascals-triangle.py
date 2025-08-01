class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==0:
            return []
        if n==1:
            return [[1]]
        if n==2:
            return [[1],[1,1]]
        k=[[1],[1,1]]
        for i in range(n-2):
            p=[1]
            l=k[-1]
            for i in range(len(k[-1])-1):

                p.append(l[i]+l[i+1])
            p.append(1)
            k.append(p)
        return k