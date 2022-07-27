class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 9999999999
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif (prices[i] - minprice > maxprofit):
                maxprofit = prices[i] - minprice
        return maxprofit

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
