class Solution:
    def sumDivisibleByK(self, nums: List[int], ke: int) -> int:
        k={}
        ans=0
        for i in nums:
            k[i]=k.get(i,0)+1
        for i in k:
            if k[i]%ke==0:
                ans+=k[i]*i
        print(k)
        return ans