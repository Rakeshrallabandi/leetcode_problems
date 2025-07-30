class Solution:
    def insert(self, inte: List[List[int]], newInte: List[int]) -> List[List[int]]:

        inte.append(newInte)
        l=[]
        inte.sort()
        l.append(inte[0])
        
        for i in range(1,len(inte)):
            
            if l and  l[-1][1] >= inte[i][0]:
                l[-1][1] = max(l[-1][1], inte[i][1])
            else:
                l.append(inte[i])
        
        return l

            