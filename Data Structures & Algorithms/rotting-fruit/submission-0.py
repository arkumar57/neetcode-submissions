class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        myset = set()

        queue = deque()

        rows = len(grid)
        cols = len(grid[0])

        num_fresh = 0
        mins = -1

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
                else:
                    continue
        

        if num_fresh == 0:
            return 0
        while queue:

            q_size = len(queue)
            mins += 1
            
            for _ in range(q_size):
                i, j = queue.popleft()

                for r,c in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:

                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c]== 1:
                        grid[r][c] = 2
                        num_fresh -= 1
                        queue.append((r,c))

        if num_fresh == 0:

            return mins
        else:
            return -1 




        