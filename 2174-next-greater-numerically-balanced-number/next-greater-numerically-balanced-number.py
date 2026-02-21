class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def isBalanced(num):
            k = {}
            
            for digit in str(num):
                digit = int(digit)
                k[digit] = k.get(digit, 0) + 1
            
            for digit in k:
                if k[digit] != digit:
                    return False
            
            return True
        
        num = n + 1
        
        while True:
            if isBalanced(num):
                return num
            num += 1