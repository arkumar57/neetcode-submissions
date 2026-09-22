class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_so_far = 0

        
        left = 0

        right = len(heights) - 1

        while left < right:

            max_so_far = max((right - left) * min(heights[left], heights[right]),max_so_far)

            if heights[right] > heights[left]:

                left += 1
            
            else:

                right -= 1
        
        return max_so_far



            





        

        
        