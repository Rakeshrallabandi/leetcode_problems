class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        for i in range(1<<len(nums)):
            sub=[]
            for j in range(len(nums)):
                if i&(1<<j):
                    sub.append(nums[j])
            ans.add(tuple(sub))
        ans=[list(i) for i in ans]
        ans.sort()
        return ans