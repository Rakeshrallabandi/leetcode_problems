class Solution:
    def canBeTypedWords(self, text: str, b: str) -> int:
        b=list(b)
        c=0
        text=text.split()
        for i in text:
            for j in b:
                if j in i:
                    c+=1
                    break
        return len(text)-c