class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict_a={}
        for i in arr:
            dict_a[i] = dict_a.get(i, 0) + 1
        dict_a=sorted(dict_a.items(),key=lambda x:x[1])
        print(dict_a)
        c=0
        for i,j in dict_a:
            if k==0:
                break
            else:
                if k<j:
                    k=0
                else:
                    k-=j
                    c+=1
        return len(dict_a)-c

                
            
