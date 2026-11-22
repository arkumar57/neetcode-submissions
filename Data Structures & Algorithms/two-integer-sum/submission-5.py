class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mymap = {}

        for i, j in enumerate(nums):

            if target - j in mymap:

                return [mymap[target - j], i]
            
            else:
                mymap[j] = i