class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:

            myset = set()

            for box in row:

                if box == ".":

                    continue
                
                elif int(box) in myset:

                    return False

                else:

                    myset.add(int(box))
                
        
        for i in range(0, len(board)):

            myset = set()

            for row in board:

                box = row[i]

                if box == ".":

                    continue

                elif int(box) in myset:

                    return False
                
                else:

                    myset.add(int(box))
                
        myset = [set() for _ in range(9)]
        for r in range(0, 9):

            for c in range(0, 9):

                value = board[r][c]

                if value == ".":

                    continue

                cell = ((r//3)*3) + (c//3)

                if value in myset[cell]:

                    return False

                else:

                    myset[cell].add(value)




       

        return True




                


        