class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            current_price = prices[i]
            if current_price > min_price:
                profit = current_price - min_price
                if profit > max_profit:
                    max_profit =  profit
            else:
                min_price = current_price
        return max_profit