class Solution:
    def construct2DArray(self, nums: List[int], m: int, n: int) -> List[List[int]]:
        k=[]
        for i in range(0,len(nums)-n+1,n):
            k.append(nums[i:i+n])
            print(nums[i:i+n],i,i+n)
        if len(k)!=m or len(k)*len(k[0])!=len(nums):
            return []
        return k
