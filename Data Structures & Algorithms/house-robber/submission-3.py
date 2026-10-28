class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [-1] * (n)

        def dfs(n):

            if n < 0:
                return 0
            
            if n == 0:
                return nums[0]
            
            if dp[n] != -1:
                return dp[n]
            
            pick = nums[n] + dfs(n - 2)
            not_pick = 0 + dfs(n -1)

            dp[n] = max(pick, not_pick)

            return dp[n]
        
        return dfs(n-1)

        