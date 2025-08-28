class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        k=[0]*32
        l=[0]*32
        i=0
        while i!=31 and start:
            k[31-i]=start%2
            start //=2
            i+=1
        i=0
        while i!=31 and goal:
            l[31-i]=goal%2
            goal //=2
            i+=1
        print(k,l)
        c=0
        for i in range(31,-1,-1):
            if l[i]^k[i]:
                c+=1
        return c
