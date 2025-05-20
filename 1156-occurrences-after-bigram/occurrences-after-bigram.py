class Solution:
    def findOcurrences(self, text: str, f: str, s: str) -> List[str]:
        # ans=[]
        text=text.split()
        # for i in range(len(text)-2):
        #     if (i+2)<len(text) and text[i]==f and text[i+1]==s:
           
        #         ans.append(text[i+2])
                
        return [text[i+2] for i in range(len(text)-2) if (i+2)<len(text) and text[i]==f and text[i+1]==s]
