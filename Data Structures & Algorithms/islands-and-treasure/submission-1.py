class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visit = set()

        def addRoom(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or grid[r][c] == -1:
                return

            visit.add((r, c))

            queue.append([r, c])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visit.add((i, j))

        dist = 0

        while queue:
            for _ in range(len(queue)):
                j, k = queue.popleft()

                grid[j][k] = dist
                addRoom(j, k + 1)
                addRoom(j, k - 1)
                addRoom(j - 1, k)
                addRoom(j + 1, k)

            dist += 1
