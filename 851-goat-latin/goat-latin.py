class Solution(object):
    def toGoatLatin(self, s):
        """
        :type sentence: str
        :rtype: str
        """
        s=s.split()
        a=set(['a','e','i','o','u'])
        c=0
        ans=[]
        for i in s:
            if i[0].lower() in a:
                n=i+'maa'+("a"*c)
            else:
                n=i[1:]+i[:1]+'maa'+("a"*c)
            ans.append(n)
            c+=1
        return ' '.join(ans)