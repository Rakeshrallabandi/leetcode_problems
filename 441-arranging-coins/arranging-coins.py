class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        ans=0
        while n>=i:
            ans+=1
            n-=i
            i+=1
        return ans