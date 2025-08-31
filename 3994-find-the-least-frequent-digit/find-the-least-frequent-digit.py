class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        k=defaultdict(int)
        while n:
            k[n%10]+=1
            n=n//10
        p=min(k[i] for i in k)
        ans=float('inf')
        for i in k:
            if k[i]==p:
                ans=min(ans,i)
        return ans