class Solution:
    def distributeCandies(self, c: List[int]) -> int:
        s=set(c)
        return min(len(c)//2,len(s))