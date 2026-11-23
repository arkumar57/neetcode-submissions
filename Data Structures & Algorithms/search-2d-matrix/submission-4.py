class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        rows = len(matrix)
        cols = len(matrix[0])


        r = rows - 1

        l = 0

        chosen_row = float('inf')
        while l <= r:

            mid = (l + r) // 2

            if matrix[mid][cols -1] < target:

                l = mid + 1
            else:

                if matrix[mid][0] > target:
                    
                    r = mid - 1
                
                else:
                    chosen_row = mid
                    break
        
        if l > r:
            return False
        l = 0
        r = cols - 1

        while l <= r:

            mid = (l + r) // 2

            if matrix[chosen_row][mid] == target:

                return True
            
            elif matrix[chosen_row][mid] > target:

                r = mid - 1
            
            else:
                l = mid + 1
        

        return False
            


        


        