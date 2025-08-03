class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                a = all(nums[i] < nums[i+1] for i in range(0, p))
                b = all(nums[i] > nums[i+1] for i in range(p, q))
                c = all(nums[i] < nums[i+1] for i in range(q, n-1))
                if a and b and c:
                    return True
        return False
