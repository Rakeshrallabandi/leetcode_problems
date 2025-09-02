from typing import List

class Solution:
    
    def mni(self,k):
        c=0
        p=[]
        ans=0
        m=0
        sumof=0
        length=0
        keys=sorted(k.keys())
        for i in keys:
            if c==0:       #minimum
                p.append(i/1)
            if c==len(keys)-1: # maximum
                p.append(i/1)
            c+=1
            if m<k[i]: # mode
                ans=i
                m=k[i]
            sumof+=i*k[i]
            length+=k[i]
        p.append(sumof/length) # mean
        p.append(ans/1)        
        return p

    def median(self,k):
        length=sum(k[i] for i in k)
        keys=sorted(k.keys())
        pri=[0]*len(keys)
        dict_a={}
        c=0
        for i in keys:
            if c==0:
                pri[c]=k[i]
            else:
                pri[c]=pri[c-1]+k[i]
            dict_a[i]=pri[c]
            c+=1
        ans=0
        if length%2!=0:  # odd
            key=(length+1)//2
            for i in dict_a:
                if dict_a[i]>=key:
                    ans=i
                    break
        else:  # even
            j=0
            key1=length//2
            key2=key1+1
            first=None
            second=None
            for i in dict_a:
                if first is None and dict_a[i]>=key1:
                    first=i
                if second is None and dict_a[i]>=key2:
                    second=i
                if first is not None and second is not None:
                    break
                j+=1
            ans=(first+second)/2
        return ans/1

    def sampleStats(self, count: List[int]) -> List[float]:
        k={}
        for i in range(len(count)):
            if count[i]:
                k[i]=count[i]
        ans=self.mni(k)
        ans.insert(3,(self.median(k)))
        return ans
