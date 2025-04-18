
class Solution:
    def hel(self,s):
        c=1
        u=[]
        t=s[0]
        for i in range(1,len(s)):

            if s[i]==s[i-1]:
                c+=1
            else:
                u.append(str(c))
                u.append(t)
                t=s[i]
                c=1
        u.append(str(c))
        u.append(t)
        return ''.join(u)
    def countAndSay(self, n: int) -> str:
        s='1'
        if n==1:
            return "1"
        else:
            for i in range(1,n):
                s=self.hel(s)
                print(s)
            return s