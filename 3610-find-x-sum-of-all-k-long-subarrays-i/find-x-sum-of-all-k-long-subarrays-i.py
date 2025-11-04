class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        temp = []
        dic = {}
        for i in range(k):
            dic[nums[i]] = dic.get(nums[i], 0) + 1

        def call(dic):
            d = sorted(dic.items(), key=lambda y: (-y[1], -y[0]))
            ans = 0
            for i in range(min(x, len(d))):
                ans += d[i][0] * d[i][1]
            return ans

        temp.append(call(dic))
        for i in range(k, len(nums)):
            dic[nums[i - k]] -= 1
            if dic[nums[i - k]] == 0:
                del dic[nums[i - k]]
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            temp.append(call(dic))
        return temp
