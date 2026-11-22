class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)

        longest_sequence = 0

        for num in nums:

            if num - 1 not in nums:

                start = num
                count = 1
                while start + 1 in nums:

                    start = start + 1
                    count += 1
                
                longest_sequence = max(longest_sequence, count)
        

        return longest_sequence




