class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        k={}
        p=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            s=''
            for j in i:
                s+=p[ord(j)-ord('a')]
            if s in k:
                k[s]+=1
            else:
                k[s]=1
        print(k)
        return len(k)


