class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
       
        k={}
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1]) not in k:
                k[abs(arr[i]-arr[i-1])]=[]
            k[abs(arr[i]-arr[i-1])].append([arr[i-1],arr[i]])
            
        m=min(i for i in k)
        return k[m]