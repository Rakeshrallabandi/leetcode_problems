class Solution:
    def doesAliceWin(self, s: str) -> bool:
        k=set(['a','e','i','o','u'])
        c=0
        for i in s:
            if i in k:
                c+=1
        return c>0