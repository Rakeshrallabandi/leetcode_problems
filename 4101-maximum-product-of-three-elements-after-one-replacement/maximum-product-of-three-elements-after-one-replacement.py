class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        a=max(((10**5)*nums[1]*nums[0]),((-10**5)*nums[1]*nums[0]))
        b=max(((10**5)*nums[0]*nums[-1]),((-10**5)*nums[0]*nums[-1]))
        c=max(((10**5)*nums[-1]*nums[-2]),((-10**5)*nums[-1]*nums[-2]))
        print(nums)
        print(a,b,c)
        return max(a,b,c)
