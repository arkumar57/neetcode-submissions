class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:



        cache = [float('inf')] * (amount + 1)

        cache[0] = 0
        
        for i in range(1, amount + 1):

            for c in coins:

                if i-c >= 0:
                    cache[i] = min(cache[i], 1 + cache[i - c])


        if cache[amount] == float('inf'):

            return -1
        
        else:
            return cache[amount]
        