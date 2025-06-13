class Solution(object):
    def maxRepeating(self, s, w):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        ans=0
        for i in range(len(s)):
            c=0
            for j in range(i,len(s)-len(w)+1,len(w)):
                if s[j:j+len(w)]==w:
                    c+=1
                else:
                    break
            ans=max(ans,c)
        return ans