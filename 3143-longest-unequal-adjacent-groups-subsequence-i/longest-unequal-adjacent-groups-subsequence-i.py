class Solution:
    def getLongestSubsequence(self, word: List[str], groups: List[int]) -> List[str]:
        k={}
        ans=[]
        for i in range(len(groups)):
            c= 0 if groups[i]==0 else 1 
            l=[]
            for j in range(i,len(groups)):
                if groups[j]==0 and c==0:
                    l.append(word[j])
                    c=1
                elif groups[j]==0 and c==1:
                    continue
                if groups[j]==1 and c==1:
                    l.append(word[j])
                    c=0
                else:
                    continue
            if len(ans)<len(l):
                ans=l[:]
                l=[]
        return ans   

