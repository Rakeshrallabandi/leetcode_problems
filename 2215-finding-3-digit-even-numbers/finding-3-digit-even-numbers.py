class Solution(object):
    def findEvenNumbers(self, d):
        """
        :type d: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        k = Counter(d)
        ans = []

        for i in range(100, 1000, 2):  
            digits = [int(x) for x in str(i)]
            p = Counter(digits)

            if all(p[x] <= k[x] for x in p):
                ans.append(i)

        return ans
