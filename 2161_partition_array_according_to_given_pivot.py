class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        k=[]
        for i in nums:
            if pivot>i:
                k.append(i)
        for i in nums:
            if pivot==i:
                k.append(i)
        for i in nums:
            if pivot<i:
                k.append(i)
        return k