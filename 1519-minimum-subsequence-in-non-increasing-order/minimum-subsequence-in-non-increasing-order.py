class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n=sorted(nums,reverse=True)
        s=sum(n)//2
        i=0
        c=0
        while i<len(nums) and c<=s:
            c+=n[i]
            i+=1

        if i<len(nums) and c==s:
            c+=n[i]  
        return n[:i]