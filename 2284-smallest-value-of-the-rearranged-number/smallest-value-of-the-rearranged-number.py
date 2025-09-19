class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if num>=0:
            if num<10:
                return num
            num=list(str(num))
            num.sort()
            c=num.count('0')
            num[0],num[c]=num[c],num[0]
            num=''.join(num)
            return int(num)
        else:
            num*=-1
            num=list(str(num))
            num.sort(reverse=True)
            num=''.join(num)
            return int(num)*-1

