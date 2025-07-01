class Solution:
    def partitionString(self, s: str) -> List[str]:
        current_str=''
        k={}
        for i in range(len(s)):
            current_str+=s[i]
            if current_str not in k:
                k[current_str]=1
                current_str=''
        if  current_str and current_str not in k:
            k.add(current_str)
        p=[i for i in k]
        return p
        