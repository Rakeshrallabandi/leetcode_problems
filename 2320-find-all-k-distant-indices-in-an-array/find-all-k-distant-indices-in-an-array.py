class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l=set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]==key and abs(i-j)<=k:
                    l.add(i)
        l=sorted(list(l))

        return l