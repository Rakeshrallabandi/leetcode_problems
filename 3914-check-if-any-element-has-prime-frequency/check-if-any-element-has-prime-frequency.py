class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        p = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29,31, 37, 41, 43, 47, 53, 59, 61, 67, 71,73, 79, 83, 89, 97])
        k={}
        for i in nums:
            if i not in k :
                k[i]=0
            k[i]+=1
        for i in k:
            if k[i] in p :
                return True
        return False