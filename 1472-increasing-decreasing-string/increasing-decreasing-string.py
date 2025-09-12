class Solution:
    def sortString(self, s: str) -> str:
        list_alpha=[0]*26
        for i in s:
            list_alpha[ord(i)-ord('a')]+=1
        ans=''
        while sum(list_alpha)!=0:
            for i in range(26):
                if list_alpha[i]>0:
                    ans+=chr(i+ord('a'))
                    list_alpha[i]-=1
            for j in range(25,-1,-1):
                if list_alpha[j]>0:
                    ans+=chr(j+ord('a'))
                    list_alpha[j]-=1
            
        return ans