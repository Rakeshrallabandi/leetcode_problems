from collections import defaultdict
class Solution:
    def call(self,n):
        t=0
        while n>0:
            t=max(n%10,t)
            n//=10
        return t
    def maxSum(self, nums: List[int]) -> int:
        k=defaultdict(list)
        for i in nums:
            p=self.call(i)
            k[p].append(i)
        s=sorted(k.items() ,key=lambda x:x[0] ,reverse=True)
        print(s)
        ans=-1
        for i in s:
            
            if len(i[1])>1:
                p=sorted(i[1],reverse=True)
                ans=max( p[0]+p[1],ans)
        return ans

