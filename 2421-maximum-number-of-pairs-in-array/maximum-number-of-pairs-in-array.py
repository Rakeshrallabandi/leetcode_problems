from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        k=defaultdict(int)
        for i in nums:
            k[i]+=1
        c=0
        n=0
        for i in k:
            if k[i]%2==0:
                c+=k[i]//2
            else:
                c+=k[i]//2
                n+=k[i]%2
        return [c,n]