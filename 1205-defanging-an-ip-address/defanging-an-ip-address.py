class Solution:
    def defangIPaddr(self, a: str) -> str:
        s=''
        for i in a:
            if i=='.':
                s+='[.]'
            else:
                s+=i
        return s