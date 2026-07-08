class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        pr=0
        bp=prices[0]
        for i in range(0,n):
            if bp >= prices[i]:
                bp=prices[i]
            sp=prices[i]
            if sp-bp>=pr:
                pr = sp-bp
        return pr