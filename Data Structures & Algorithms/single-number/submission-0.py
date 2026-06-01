class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        numbers = {}

        for n in nums:

            if n not in numbers:

                numbers[n] = 1

            else:
                numbers[n] += 1

        
        for nums in numbers:

            if numbers[nums] == 1:
                return nums