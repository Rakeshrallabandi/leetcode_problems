class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            s='a'*(n-1)+'b'
            return s
        return 'a'*n