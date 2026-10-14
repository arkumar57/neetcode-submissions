class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mymap = {}
        result = []

        for num in nums:

            if num in mymap:

                mymap[num] += 1
            
            else:
                mymap[num] = 1

        
        while mymap:

            smallest_key = min(mymap)

            while mymap[smallest_key] > 0:

                result.append(smallest_key)
                mymap[smallest_key] -= 1
            
            mymap.pop(smallest_key)
        
        nums[:] = result
        

        

        