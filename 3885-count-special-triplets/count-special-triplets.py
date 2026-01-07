class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        l={}
        r={}
        count=0
        for i in nums:
            r[i]=r.get(i,0)+1
    
        for i in nums:
            r[i]-=1
            if r[i]==0:
                del r[i]
            if i*2 in l and i*2 in r:
                count+=(l[i*2]*r[i*2])
                count%=10**9 + 7
            l[i]=l.get(i,0)+1

        return count