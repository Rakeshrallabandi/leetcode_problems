class Solution:
    def resultingString(self, s: str) -> str:
        k = []
        for ch in s:
            k.append(ch)
            while len(k) >= 2:
                a, b = k[-1], k[-2]
                
                if (ord(a) - ord(b)) % 26 == 1 or (ord(b) - ord(a)) % 26 == 1:
                    k.pop()
                    k.pop()
                else:
                    break
        return ''.join(k)
