class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ans=[]
        for i in range(0,len(s),k):
            ans.append(s[i:i+k])
        print(ans)
        if len(ans[-1])!=k:
            ans[-1]=ans[-1]+((k-len(ans[-1]))*fill)    
        return ans   