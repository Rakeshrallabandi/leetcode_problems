from collections import defaultdict
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], f: int) -> List[int]:
        k=defaultdict(int)
        for i in arr:
            for j in arr:
                if i!=j:
                    k[i,j]=i/j
        p=sorted(k.items(),key=lambda x:x[1])
        
        c=0
        for i in p:
            c+=1
            if c==f:
                return i[0]
