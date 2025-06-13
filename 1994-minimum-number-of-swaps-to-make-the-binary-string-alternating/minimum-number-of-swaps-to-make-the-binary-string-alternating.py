class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        c1=s.count('1')
        c2=len(s)-c1
        if abs(c1-c2)>1:
            return -1
        t1=['0']*len(s)
        t2=['1']*len(s)
        c1,c2=0,0
        for i in range(len(s)):
            if i%2==0:
                t1[i]='1'
                t2[i]='0'
        for i in range(len(s)):
            if s[i]!=t1[i]:
                c1+=1
                print(s[i],t1[i])
            if s[i]!=t2[i]:
                c2+=1
        print(t1,t2,c1,c2)
        if c1%2==0 and c2%2==0:
            return min(c1,c2)//2
        elif c1%2==0 and c2%2!=0:
            return c1//2
        return c2//2
