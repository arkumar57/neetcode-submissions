class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        mymap = {}
        result = []

        for num in nums:

            if num not in mymap:

                mymap[num] = 1
            else:
                mymap[num] += 1
        


        while mymap:

            smallest_key = min(mymap)

            while mymap[smallest_key] > 0:

                result.append(smallest_key)
                mymap[smallest_key] -= 1
            
            mymap.pop(smallest_key)
        
        return result

        
        