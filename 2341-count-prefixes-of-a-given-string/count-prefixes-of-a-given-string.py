class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        p=''
        ans=0
        for i in s:
            p+=i
            ans+=words.count(p)
        return ans