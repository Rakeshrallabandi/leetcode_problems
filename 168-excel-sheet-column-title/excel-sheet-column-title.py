class Solution:
    def convertToTitle(self, c: int) -> str:
        result = ""
        while c > 0:
            c -= 1  
            remainder = c % 26
            result = chr(ord('A') + remainder) + result
            c //= 26
        return result