class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        p=[]
        k=[]
        s=list(s)
        se=set(['a','e','i','o','u'])
        for i in range(len(s)):
            if s[i].lower() in se:
                p.append(s[i])
                k.append(i)
        p.sort()
        j=0
        for i in k:
            s[i]=p[j]
            j+=1
        return ''.join(s)

