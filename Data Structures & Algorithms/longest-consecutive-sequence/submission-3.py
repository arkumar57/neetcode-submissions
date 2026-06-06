class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        myset = set();

        if len(nums) == 1:

            return 1

        for num in nums:

            myset.add(num)
        

        max_so_far = 0
        for num in myset:

            if num-1 not in myset:

                current = num
                length = 1

                while current+1 in myset:

                    current = current + 1
                    length += 1
                    
                max_so_far = max(max_so_far, length)

        
        return max_so_far


        

        