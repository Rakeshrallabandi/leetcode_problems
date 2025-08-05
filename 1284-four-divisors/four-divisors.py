class Solution:
    def co(self,n):
        count = 0
        ans=[]
        for i in range(1, int(math.isqrt(n)) + 1):
            if n % i == 0:
                count += 1
                ans.append(i)
                if i != n // i:
                    count += 1
                    ans.append(n//i)
        return sum(ans),count
    def sumFourDivisors(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            s,k=self.co(i)
            if k==4:
                c+=s
        return c
