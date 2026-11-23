class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_so_far = 0

        l = 0

        r = len(heights) - 1

        while l < r:

            max_so_far = max(max_so_far, min(heights[l], heights[r]) * (r - l))
            if heights[l] > heights[r]:

                r -= 1
            else:
                l += 1
        

        return max_so_far