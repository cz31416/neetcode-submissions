class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        cur_max = prices[0]
        cur_profit = 0
        for price in range(len(prices)):
            if prices[price] > cur_max:
                cur_max = prices[price]
            if prices[price] < cur_min:
                cur_profit = max(cur_profit, cur_max - cur_min)
                cur_min = prices[price]
                cur_max = prices[price]
            if price + 1 == len(prices):
                return max(cur_profit, cur_max - cur_min)