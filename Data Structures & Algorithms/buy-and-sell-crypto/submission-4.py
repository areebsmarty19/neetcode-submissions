class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        mprofit = 0
        while j <= len(prices) - 1:
            buy = prices[i]
            sell = prices[j]
            profit = sell - buy

            if profit < 0:
                i = j
                j+=1
            else:
                if profit > mprofit:
                    mprofit = profit
                j+=1
        return mprofit 