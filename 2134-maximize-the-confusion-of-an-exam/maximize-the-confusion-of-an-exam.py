from collections import deque
class Solution:
    def maxConsecutiveAnswers(self, arr: str, ka: int) -> int:
        def call(key):
            k=deque()
            i=0
            j=0
            c=0
            ans=0
            while i!=len(arr):
                
                if arr[i]==key:
                    c+=1
                if c>ka:
                    
                    while k and c>ka and k[0]!=key:
                        k.popleft()
                    k.popleft()
                    c-=1
                k.append(arr[i])
                ans=max(ans,len(k))
                i+=1
            print(k,c)
            return ans
        return max(call('T'),call('F'))
