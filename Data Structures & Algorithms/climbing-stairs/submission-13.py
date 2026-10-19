class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 2:
            return n
        cache = [-1] * (n+1)
        def dfs(i):
            if i <= 2:
                return i
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i- 1) + dfs(i - 2)
            return cache[i]

        return dfs(n)