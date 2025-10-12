class Solution:
    def longestBalanced(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            m=1
            k={}
            
            for j in range(i,len(s)):
                k[s[j]]=k.get(s[j],0)+1
                m=max(k[s[j]],m)
                if m*len(k)==j-i+1:
                    ans=max(ans,m*len(k))
                    
        return ans