class Solution:
    def maxArea(self, l: List[int]) -> int:
        m=-float('inf')
        i=0
        j=len(l)-1
        while i<j:
            m=max(min(l[i],l[j])*(j-i),m)
            if l[i]<l[j]:
                i+=1
            else:
                j-=1
        return m
