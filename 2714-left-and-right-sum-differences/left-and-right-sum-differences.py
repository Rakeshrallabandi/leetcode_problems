class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a=[0]
        for i in range(len(nums)-1):
            a.append(a[-1]+nums[i])
        b=[0]
        for i in range(len(nums)-1,0,-1):
            b.append(b[-1]+nums[i])
        print(a,b)
        b=b[::-1]
        return [abs(a[i]-b[i]) for i in range(len(a))]