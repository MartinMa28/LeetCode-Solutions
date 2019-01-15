class Solution:

    def max_profit(self, prices):
        profit = 0
        if prices != []:
            # initial value for buy and sell is the first element in the list, and they are the same
            buy = prices[0]
            current_should_sell = prices[0]
            for index, value in enumerate(prices[1:], 1):
                if value < current_should_sell:
                    # if the current value is less than sell
                    # there are two probabilities:
                    
                    # 1. you will make less money, so you should sell it
                    
                    # 2. you will lose money, because the price you buy 
                    # is greater than current value, so you should not buy
                    # on previous day, and buy it now 
                    # in this case profit won't increase, because buy and sell's 
                    # initial values are the same
                    profit += current_should_sell - buy
                    buy = value
                    current_should_sell = value
                    
                elif index == len(prices) - 1:
                    # if current value is the last element in the list
                    if value < current_should_sell:
                        # and current value is less than sell
                        # 2 probabilities again 
                        # you will earn less money, or you will lose money
                        profit += current_should_sell - buy
                    else:
                        # you can make more money by selling it today
                        profit += value - buy
                else:
                    # you can make more money
                    current_should_sell = value
        
        return profit


if __name__ == "__main__":
    solu = Solution()
    test_list = [7,1,5,3,6,4]
    test_list2 = [2 ,4, 1]
    print(solu.max_profit(test_list2))