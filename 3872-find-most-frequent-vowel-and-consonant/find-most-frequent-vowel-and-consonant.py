class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        se=set(['a','e','i','o','u'])
        vowel={}
        con={}
        for i in s:
            if i in se:
                if i in vowel:
                    vowel[i]+= 1
                else:
                    vowel[i]=1
            else:
                if i in con:
                    con[i]+=1
                else:
                    con[i]=1
        m1 = max([vowel[i] for i in vowel]) if vowel else 0
        m2 = max([con[i] for i in con]) if con else 0
        return m1 + m2

