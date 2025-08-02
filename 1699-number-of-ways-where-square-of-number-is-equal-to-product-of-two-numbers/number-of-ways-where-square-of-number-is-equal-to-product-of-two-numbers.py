class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def get_count(a, b):
            res = 0
            for i in a:
                t = i * i
                k = {}
                ans = 0
                for j in b:
                    if t % j == 0:
                        if t // j in k:
                            ans += k[t // j]
                    k[j] = k.get(j, 0) + 1
                res += ans
            return res

        c = get_count(nums1, nums2) + get_count(nums2, nums1)
        return c
