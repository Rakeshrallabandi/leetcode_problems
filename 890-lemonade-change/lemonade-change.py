class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=0
        t=0
        tw=0
        for i in bills:
            if i==5:
                f+=1
            elif i==10:
                if f>0:
                    t+=1
                    f-=1
                else:
                    return False
            else:
                if t>0 and f>0:
                    t-=1
                    f-=1
                elif f>2:
                    f-=3
                else:
                    return False
        return True  