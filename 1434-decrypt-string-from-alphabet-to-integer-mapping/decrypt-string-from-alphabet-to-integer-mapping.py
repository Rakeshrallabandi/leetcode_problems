class Solution:
    def freqAlphabets(self, s: str) -> str:
        k={}
        for i in range(ord('j')-ord('a')):
            k[str(i+1)]=chr(i+ord('a'))
        l={}
        for i in range(ord('j')-ord('a') ,ord('z')-ord('a')+1):
            l[str(i+1)+'#']=chr(i+ord('a'))
        
        for i in l:
            if i in s:
                s=s.replace(i,l[i])
                print(i,l[i])
        
        for i in k:
            if i in s:
                s=s.replace(i,k[i])
        return s
        
