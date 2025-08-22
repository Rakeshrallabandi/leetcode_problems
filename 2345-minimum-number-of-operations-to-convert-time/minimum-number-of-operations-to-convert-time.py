class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1,m1=map(int,current.split(':'))
        h2,m2=map(int,correct.split(":"))
        print(h1,m1,h2,m2)
        m1=h1*60+m1
        m2=h2*60+m2
        ans=0
        while m1<m2:
            if m1+60<=m2:
                m1+=60
            elif m1+15<=m2:
                m1+=15
            elif m1+5<=m2:
                m1+=5
            else:
                m1+=1
            ans+=1
        return ans