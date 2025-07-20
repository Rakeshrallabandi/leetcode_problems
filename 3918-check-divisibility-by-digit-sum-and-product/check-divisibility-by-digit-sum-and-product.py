class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n<10:
            return False
        s=0
        p=1
        m=n
        while n!=0:
            r=n%10
            n//=10
            s+=r
            p*=r
        if m%(s+p)==0:
            return True
        return False