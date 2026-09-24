class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        if len(prices) == 0:

            return

        buyday = prices[0]
        sellday = prices[0]

        max_profit_so_far = 0


        for i in range(1, len(prices)):

            if prices[i] < buyday:

                buyday = prices[i]

                sellday = prices[i]

                max_profit_so_far = max(max_profit_so_far, sellday - buyday)
            
            elif prices[i] >= sellday:

                sellday = prices[i]

                max_profit_so_far = max(max_profit_so_far, sellday - buyday)

            else:

                continue
        

        return max_profit_so_far


                

            



        
        