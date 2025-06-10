class Solution(object):
    def maxSumDistinctTriplet(self, x, y):
        """
        :type x: List[int]
        :type y: List[int]
        :rtype: int
        """
        # from collections import defaultdict

        hashmap = defaultdict(int)
        n = len(x)

        for i in range(n):
            hashmap[x[i]] = max(hashmap[x[i]], y[i])

        if len(hashmap) < 3:
            return -1

   
        vals = sorted(hashmap.values(), reverse=True)
        return vals[0] + vals[1] + vals[2]
        