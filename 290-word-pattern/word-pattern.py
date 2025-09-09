class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        #print(set(list(pattern)),set(split(s)))
        if len(set(list(pattern)))!=len(set(s.split())) or len(pattern) !=len(s.split()):
            return False
        k=['']*26
        p=0
        # print(pattern, s)
        for i,j in enumerate(s.split()):
            o=ord(pattern[p])-ord('a')
            if k[o]=='':
                k[o]=j
            elif k[o]!=j:
            #     continue
            # else:
            #     print(k)
                return False
            p+=1
            # print(k)
        return True