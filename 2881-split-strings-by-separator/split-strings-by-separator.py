class Solution:
    def splitWordsBySeparator(self, words: List[str], s: str) -> List[str]:
        ans=[]
        for i in words:
            ans+=[j for j in i.split(s) if j]
        return ans