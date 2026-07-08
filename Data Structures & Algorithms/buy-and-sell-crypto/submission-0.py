class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        for i in range(0,n):
            for j in range(i,n):
                if prices[j]-prices[i]>=profit:
                    profit=prices[j]-prices[i]
                else:
                    continue
        return profit