class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)


        for i in range(len(nums)):

            all_prev = nums[:i]

            all_next = nums[i+1:]


            for p in all_prev:

                if p == 0:

                    output[i] = 0
                
                else:
                    
                    output[i] *= p
            
            for n in all_next:

                if n == 0:

                    output[i] = 0
                else:

                    output[i] *= n

            # if nums[i] != 0:

            #     output[i] = output[i] // nums[i]
 
        
        return output

        
        