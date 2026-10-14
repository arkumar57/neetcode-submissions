class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mymap = {}

        for i in range(len(nums)):

            if nums[i] in mymap:

                return True
            else:
                mymap[nums[i]] = 1
        

        return False
        