class Solution:
    def minimumBuckets(self, h: str) -> int:
        h=list(h)
        if h.count('H')==len(h):
            return -1
        if len(h)>2 and ((h[0]==h[1]=='H') or h[-1]==h[-2]=='H'):
            return -1
        for i in range(1,len(h)-1):
            if h[i]=='H' and h[i-1]=='H' and h[i+1]=='H':
                return -1
        for i in range(len(h)):
            if h[i]=='H':
                if (i<len(h)-1 and h[i+1]=='T') or ( i>0 and h[i-1] =='T'):
                    continue

                if i<len(h)-1 and h[i+1]=='.':
                    h[i+1]='T'
                elif i>0 and h[i-1] =='.':
                    h[i-1]='T'
        print(h)
        
        return h.count('T')