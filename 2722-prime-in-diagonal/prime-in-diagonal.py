class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        prime = []
        n = len(nums)
        for i in range(n):
            prime.append(nums[i][i])             # Main diagonal
            prime.append(nums[i][n - 1 - i])     # Anti-diagonal

        ans = 0
        for i in prime:
            if i < 2:
                continue
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                ans = max(ans, i)
        return ans
