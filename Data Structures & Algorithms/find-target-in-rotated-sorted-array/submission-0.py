class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0

        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if target == nums[mid]:

                return mid


            if nums[mid] >= nums[left]:
            
            #in the left section
                if target >= nums[left] and target < nums[mid]:
                    
                    right = mid - 1
                else:
                    left = mid + 1

            else:

            #in the right section

                if target > nums[mid] and target <= nums[right]:

                    left = mid + 1

                else:

                    right = mid - 1  
        

        return -1

        

        
        