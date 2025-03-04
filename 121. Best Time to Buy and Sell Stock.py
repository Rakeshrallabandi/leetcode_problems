class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans=0
        buy=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            elif prices[i]-buy>ans:
                ans=prices[i]-buy   
        return ans
                 