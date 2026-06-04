class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        my_dict = {}

        result = []

        for num in nums:

            if num not in my_dict:

                my_dict[num] = 1
            
            else:

                my_dict[num] += 1

        
        while(k != 0):

            result.append(max(my_dict, key = my_dict.get))

            del my_dict[max(my_dict, key = my_dict.get)]

            k -= 1;
        

        return result;

            
    
        