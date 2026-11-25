class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque()

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 0:

                    queue.append([i, j])
        

        while queue:

            x, y = queue.popleft()

            points = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]

            for a,b in points:

                if a < 0 or a >= len(grid) or b < 0 or b >= len(grid[0]) or grid[a][b] == -1 or grid[a][b] == 0:

                    continue
                
                elif grid[a][b] == 2147483647:

                    grid[a][b] = min(grid[a][b], grid[x][y] + 1)

                    queue.append([a,b])
                    
        





