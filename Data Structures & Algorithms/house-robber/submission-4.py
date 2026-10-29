class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_line(arr):

            n = len(nums)

            dp = [-1] * (n)


            def dfs(i):

                if i < 0:
                    return 0
                
                if i == 0:
                    return nums[0]
                
                if dp[i] != -1:
                    return dp[i]
                
                pick = nums[i] + dfs(i - 2)
                not_pick = 0 + dfs(i -1)

                dp[i] = max(pick, not_pick)

                return dp[i]
        
            return dfs(n-1)

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))

        