class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=prices[0]
        for r in range(1,len(prices)):
            profit=max(profit,prices[r]-l)
            if prices[r]<l:
                l=prices[r]
        return profit
            