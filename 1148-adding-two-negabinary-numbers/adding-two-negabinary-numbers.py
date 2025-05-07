class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        ans=0
        ans1=0
        for i, bit in enumerate(reversed(arr1)):
            ans+=bit*((-2)**i)
        for j ,bit1 in enumerate(reversed(arr2)):
            ans1+=bit1*((-2)**j)
        n=ans1+ans
        result = []
        while n != 0:
            n, rem = divmod(n, -2)
            if rem < 0:
                rem += 2
                n += 1
            result.append(rem)
        return result[::-1] if len(result)!=0 else [0]