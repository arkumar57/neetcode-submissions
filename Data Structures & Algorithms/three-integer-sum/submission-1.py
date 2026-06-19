class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []

        for i in range(0, len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            
            right = len(nums) - 1

            target = -nums[i]

            while left < right:

                if nums[left] + nums[right] < target:

                    left += 1

                elif nums[left] + nums[right] > target:

                    right -= 1

                else:

                    new_result = []
                    new_result.append(nums[i])
                    new_result.append(nums[left])
                    new_result.append(nums[right])

                    result.append(new_result)

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        

        return result


        