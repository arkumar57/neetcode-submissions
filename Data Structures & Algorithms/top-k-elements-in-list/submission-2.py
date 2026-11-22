class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mymap = {}

        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:

            if num not in mymap:

                mymap[num] = 1

            else:
                mymap[num] += 1
        
        for num,count in mymap.items():

            bucket[count].append(num)
        

        res = []

        for j in range(len(bucket) - 1, 0, -1):

            for n in bucket[j]:
                res.append(n)
                if len(res) == k:

                    return res


        
         
        
