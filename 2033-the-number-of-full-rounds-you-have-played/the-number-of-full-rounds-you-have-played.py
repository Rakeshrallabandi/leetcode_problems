class Solution:
    def numberOfRounds(self, login: str, logout: str) -> int:
        f1 = int(login[:2])
        f2 = int(login[3:])
        s1 = int(logout[:2])
        s2 = int(logout[3:])
        start = f1 * 60 + f2
        end = s1 * 60 + s2
        if end < start:
            end += 24 * 60
        if start % 15 != 0:
            start += 15 - (start % 15)
        end -= end % 15
        if end < start:
            return 0
        return (end - start) // 15
