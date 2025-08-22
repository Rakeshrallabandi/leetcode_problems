class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        p=''
        n=len(s)
        k=k%n
        for i in range(n):
            p+=s[(i+k)%n]
        return p