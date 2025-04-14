class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1 or len(s)==2:
            return s
        else:
            l=list(s)
            l.sort()
            k=['']*(len(l))
            p1=0
            p2=len(l)-1
            i=0
            f=''
            while i!=(len(l)):
                if i+1!=len(l) and l[i]==l[i+1]:
                    k[p1]=l[i]
                    k[p2]=l[i]
                    p1+=1
                    p2-=1
                    i+=2
                else:
                    f=l[i]
                    i+=1
            
            if f:
                for i in range(len(k)):
                    if k[i]=='':
                        k[i]=f
                        break
            return ''.join(k)