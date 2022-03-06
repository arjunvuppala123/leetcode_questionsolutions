class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,summation = 0,0
        minimum = prices[0]
        for price in prices:
            if price < minimum:
                minimum = price
            elif price > minimum:
                summation = price-minimum
            if summation > profit:
                profit = summation
        return profit