class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def build(r, b):
            i = 1
            h = 0
            turn_red = True
            while True:
                if turn_red:
                    if r >= i:
                        r -= i
                        h += 1
                        i += 1
                        turn_red = False
                    else:
                        break
                else:
                    if b >= i:
                        b -= i
                        h += 1
                        i += 1
                        turn_red = True
                    else:
                        break
            return h

        return max(build(red, blue), build(blue, red))
