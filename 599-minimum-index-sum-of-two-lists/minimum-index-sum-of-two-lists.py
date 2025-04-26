class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        k={}
        p={}
        for i in range(len(list1)):
            k[list1[i]]=i
        for j in range(len(list2)):
            if list2[j] in k:
                p[list2[j]]=k[list2[j]]+j
        
        u=float('inf')
        ans=[]
        for i in p:
            u=min(u,p[i])
        for i in p:
            if p[i]==u:
                ans.append(i)
        return ans