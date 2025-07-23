class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s, first, second, value):
            stack = []
            points = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    points += value
                else:
                    stack.append(ch)
            return ''.join(stack), points

        ans = 0
        if x > y:
            s, gained = remove_pair(s, 'a', 'b', x)
            ans += gained
            _, gained = remove_pair(s, 'b', 'a', y)
            ans += gained
        else:
            s, gained = remove_pair(s, 'b', 'a', y)
            ans += gained
            _, gained = remove_pair(s, 'a', 'b', x)
            ans += gained

        return ans
