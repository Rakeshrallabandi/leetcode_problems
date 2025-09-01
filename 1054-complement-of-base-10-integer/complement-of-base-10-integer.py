class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=bin(n)[2:]
        a=''
        for i in s:
            if i=='0':
                a+='1'
            else:
                a+='0'
        return int(a,2)
