class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        p=[""]*len(s)
        i=0
        j=len(s)-1
        
        while i<=j:
            
            m=min(s[i],s[j])
            p[i]=m
            p[j]=m
            i+=1
            j-=1
        return ''.join(p)