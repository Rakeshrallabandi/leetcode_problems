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
        l=sorted(p.items(),key=lambda x:x[1])
        u=float('inf')
        ans=[]
        for i in l:
            u=min(u,i[1])
        for i in l:
            if i[1]==u:
                ans.append(i[0])
        return ans