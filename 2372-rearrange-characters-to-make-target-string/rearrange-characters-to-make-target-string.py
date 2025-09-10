class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        k={}
        for i in s:
            if i in k:
                k[i]+=1
            else:
                k[i]=1
        ans=float('inf')
        l={}
        for i in target:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        for i in target:
            if i in k and k[i]>=l[i]:
                ans=min(ans,k[i]//l[i])
            else:
                return 0
        return ans