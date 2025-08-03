class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        k=[-1]*(len(nums))
        p=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            k[i]=max(k[i+1],p)
            p=max(k[i],nums[i])
        print(k)
        return k
