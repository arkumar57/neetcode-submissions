class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        subarray = {0:1}
        prefixsum = 0
        count = 0

        for i in nums:
            
            prefixsum += i
            diff = prefixsum - k
            count += subarray.get(diff, 0)
            if prefixsum not in subarray:
                subarray[prefixsum] = 1
            else:

                subarray[prefixsum] += 1
            # subarray[prefixsum] = 1 + subarray.get(prefixsum, 0)
        
        return count

        