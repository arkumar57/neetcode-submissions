class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()

        counter = 0
        
        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 2:

                    queue.append([i, j])
                
                elif grid[i][j] == 1:
                    counter += 1
                else:
                    continue

        
        mins = 0
        while queue:

            size = len(queue)

            for i in range(size):
                
                x, y = queue.popleft()

                points = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

                for a, b in points:

                    if a < 0 or a >= len(grid) or b < 0 or b >= len(grid[0]):

                        continue
                
                    else:

                        if grid[a][b] == 1:

                            grid[a][b] = 2

                            counter -= 1
                            queue.append([a,b])
            
            if len(queue) > 0:

                mins += 1
        
        if counter > 0:

            return -1
        
        else:
            return mins

        # return mins
            


        


