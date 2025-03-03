class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[]
        k=[]
        for i in nums:
            if i<0:
                k.append(i)
            else:
                p.append(i)
        if len(p)==0:
            return k
        elif len(k)==0:
            return  p
        else:
            ans=[]
            i=0
            while i!=len(k):
                ans.append(p[i])
                ans.append(k[i])
                i+=1
            return ans
            