class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even={}
        odd={}
        even_count=0
        odd_count=0
        for i in range(len(nums)):
            if i%2==0:
                even[nums[i]]=even.get(nums[i],0)+1
                even_count+=1
            else:
                odd[nums[i]]=odd.get(nums[i],0)+1
                odd_count+=1
        if len(set(nums))==1:
            return min(odd_count,even_count)
        odd=sorted(odd.items(),key=lambda x:x[1],reverse=True)
        even=sorted(even.items(),key=lambda x:x[1], reverse=True)
        print(even,'\n',odd)
        if odd[0][0]!=even[0][0]:
            ans=odd_count-odd[0][1]
            ans+=even_count-even[0][1]
            return ans
        else:
            p1=odd_count-odd[1][1]+even_count-even[0][1] if len(odd)>1 else float('inf')
            p2=odd_count-odd[0][1]+even_count-even[1][1] if len(even)>1 else float('inf')
            return min(p1,p2)
