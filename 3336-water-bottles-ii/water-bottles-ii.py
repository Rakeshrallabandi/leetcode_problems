class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        empty=numBottles
        numBottles=0
        while numBottles or empty>=numExchange:
            if numExchange<=empty:
                empty-=numExchange
                
                numExchange+=1
                numBottles+=1
            if numBottles:
                ans+=numBottles
                empty+=numBottles
                numBottles=0
        return ans
            
