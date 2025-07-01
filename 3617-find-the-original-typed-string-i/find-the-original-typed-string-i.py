class Solution:
    def possibleStringCount(self, w: str) -> int:
        
        ans=0
        c=0
        for i in range(1,len(w)):
            if w[i]==w[i-1]:
                c+=1
                #print(w[i],w[i-1])
            else:
                ans+=c
                c=0
        
        return ans+1+c