class Solution:
    def tribonacci(self, n: int) -> int:

        if n <= 1:
            return n

        cache = [-1] * (n + 1)

        cache[0] = 0
        cache[1] = 1
        cache[2] = 1

        def dfs(n):

            if cache[n] != -1:
                return cache[n]

            cache[n] = dfs(n - 3) + dfs(n - 2) + dfs(n - 1)

            return cache[n]
        
        return dfs(n)
        