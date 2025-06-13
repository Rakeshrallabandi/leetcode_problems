class Solution:
    def thousandSeparator(self, n: int) -> str:
        n=str(n)
        if len(n)<4:
            return n
        t=[]
        for i in range(len(n) - 1, -1, -3):
            t.append(n[max(0, i - 2):i + 1])
        t='.'.join(t[::-1])
        if t[0]=='.':
            return t[1:]
        return t