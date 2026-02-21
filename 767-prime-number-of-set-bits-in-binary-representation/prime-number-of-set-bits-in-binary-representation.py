class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        l=[2,3,5,7,11,13,17,19,23,29,31]
        ans=0
        for i in range(left,right+1):
            n=bin(i)
            if n.count('1') in l:
                ans+=1
        return ans