class Solution(object):
    def findFinalValue(self, nums, o):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        s=set(nums)
        while o in s:
            o=o*2
        return o