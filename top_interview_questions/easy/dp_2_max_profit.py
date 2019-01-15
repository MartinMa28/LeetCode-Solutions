class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')

        for cur_price in prices:
            min_price = min(cur_price, min_price)
            max_profit = max(max_profit, cur_price - min_price)
        
        return max_profit