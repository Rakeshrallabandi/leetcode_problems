class Solution:
    def divideArray(self, nums: List[int], key: int) -> List[List[int]]:
        nums.sort()
        ans = []
        k = [nums[i:i+3] for i in range(0, len(nums), 3)] 

        for group in k:
            
            if group[2] - group[0] <= key:  
                ans.append(group)
            else:
                return []   
        
        return ans
