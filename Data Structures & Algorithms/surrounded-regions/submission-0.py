class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(i, j):

            if i >= 0 and i < rows and j >= 0 and j < cols and (i,j) not in visited and board[i][j] == "O":
                visited.add((i, j))
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        
        for c in range(cols):

            if board[0][c] == 'O':

                if (0, c) not in visited:
                    dfs(0, c)
            
            if board[rows - 1][c] == 'O':

                if (rows - 1, c) not in visited:

                    dfs(rows - 1, c)
            
            else:
                continue
        
        for r in range(rows):

            if board[r][0] == 'O':

                if (r, 0) not in visited:

                    dfs(r, 0)
            
            if board[r][cols - 1] == 'O':

                if (r, cols - 1) not in visited:

                    dfs(r, cols - 1)
            
            else:
                continue
        

        for r in range(rows):

            for c in range(cols):

                if board[r][c] == "O" and (r,c) not in visited:

                    board[r][c] = "X"
        

        
                






        