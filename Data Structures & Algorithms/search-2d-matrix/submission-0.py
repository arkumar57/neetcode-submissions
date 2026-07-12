class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0

        right = len(matrix) - 1

        while left <= right:

            mid = left + (right - left) // 2

            inner_left = 0

            inner_right = len(matrix[mid]) - 1

            while inner_left <= inner_right:
    

                inner_mid = inner_left + (inner_right - inner_left) // 2

                if matrix[mid][inner_mid] == target:

                    return True
                
                elif target < matrix[mid][inner_mid]:

                    inner_right = inner_mid - 1
                
                else:

                    inner_left = inner_mid + 1
            
            if target < matrix[mid][0]:

                right = mid - 1
            else:

                left = mid + 1

            


        

        return False

        

        
        