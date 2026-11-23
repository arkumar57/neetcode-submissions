class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buyday = prices[0]
        sellday = prices[0]

        i = 1
        max_so_far = 0
        while i < len(prices):

            if prices[i] < buyday:

                buyday = prices[i]
                sellday = prices[i]

            
            elif prices[i] > sellday:

                sellday = prices[i]

                max_so_far = max(max_so_far, sellday - buyday)
            
            i+=1
        
        return max_so_far
