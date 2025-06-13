class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count('1')
        zeros = len(s) - ones

        if abs(ones - zeros) > 1:
            return -1

        # Count mismatched positions for both patterns
        # Pattern 0: 010101...
        # Pattern 1: 101010...
        count_pat0 = 0
        count_pat1 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    count_pat0 += 1
                else:
                    count_pat1 += 1
            else:
                if s[i] == '0':
                    count_pat0 += 1
                else:
                    count_pat1 += 1

        if ones == zeros:
            return min(count_pat0 // 2, count_pat1 // 2)
        elif ones > zeros:
            return count_pat1 // 2
        else:
            return count_pat0 // 2
