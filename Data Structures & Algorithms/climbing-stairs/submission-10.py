class Solution:
    def __init__(self):
        self.dp = {}
    def climbStairs(self, n: int) -> int:

        if n <= 2:

            return n
        dp = [-1] * (n + 1)
        
        if n in self.dp:
            return self.dp[n]
        else:
            self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.dp[n]
        




        
        