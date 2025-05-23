class Solution(object):
    def minCost(self, c, n):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        i=1
        c=list(c)
        ans=0
        while i!=len(c):
            if c[i]==c[i-1]:
                if n[i]>n[i-1]:
                    ans+=n[i-1]
                    c.pop(i-1)
                    n.pop(i-1)
                else:
                    ans+=n[i]
                    c.pop(i)
                    n.pop(i)
            else:
                i+=1
        return ans

        