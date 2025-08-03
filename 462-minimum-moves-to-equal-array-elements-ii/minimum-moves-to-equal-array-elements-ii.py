class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def call(array,n):
            ans=0
            print(n)
            for i in array:
                ans+=abs(n-i)
            return ans
        nums.sort()
        k=len(nums)
        if k==1:
            return 0
        if k==2:
            return abs(nums[0]-nums[1])
        if len(nums)%2==0:
            
            return min(call(nums,nums[k//2]),call(nums,nums[(k//2)+1]))
        return call(nums,nums[k//2])