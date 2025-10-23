class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            
            even={}
            odd={}
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    even[nums[j]]=even.get(nums[j],0)+1
                else:
                    odd[nums[j]]=odd.get(nums[j],0)+1

                if len(even)==len(odd):
                    ans=max(ans, j-i+1)
        return ans