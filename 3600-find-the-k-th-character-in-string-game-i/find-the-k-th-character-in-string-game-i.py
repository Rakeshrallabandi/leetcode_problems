class Solution:
    def kthCharacter(self, k: int) -> str:
        s='a'
        while len(s)<=k:
            p=''
            for i in s:
                p+=chr((ord(i)-ord('a')+1)%26+ord('a'))
            s+=p
        print(s)
        return s[k-1]