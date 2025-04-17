class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        k={}
        for i in strs:
            l=list(i)
            l.sort()
            l=''.join(l)
            if l in k:
                k[l].append(i)
            else:
                k[l]=[i]
        ans=[]
        for i in k:
            ans.append(k[i])
        ans.sort()
       
        return ans