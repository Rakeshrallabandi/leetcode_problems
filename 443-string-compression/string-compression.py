class Solution:
    def compress(self, chars: List[str]) -> int:
        k=1
        s=chars[0]
        ans=[]
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                k+=1
                s=chars[i]
            else:
                if k>1:
                    ans.append(s)
                    for p in list(str(k)):
                        ans.append(p)
                else:
                    ans.append(s)
                k=1
                s=chars[i+1]
        if s:
            if k>1:
                    ans.append(s)
                    for p in list(str(k)):
                        ans.append(p)
            else:
                ans.append(s)
        chars[:]=ans[:]
