class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        a=set()
        for i in range(10):
            a.add(str(i))
        ans=-float('inf')
        for i in strs:
            k=0
            for j in range(len(i)):
                if i[j] not in a:
                    k=1
                    break
            if k==1:
                ans=max(ans,len(i))
            else:
                ans=max(ans,int(i))
        return ans
