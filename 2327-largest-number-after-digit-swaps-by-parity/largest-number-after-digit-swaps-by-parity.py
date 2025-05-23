class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        o = sorted([d for d in s if int(d) % 2], reverse=True)
        e = sorted([d for d in s if int(d) % 2 == 0], reverse=True)
        return int(''.join(o.pop(0) if int(d) % 2 else e.pop(0) for d in s))
