class Solution:
    def hammingWeight(self, n: int) -> int:

        result = bin(n)

        count = 0

        for i in range(2, len(result)):

            if result[i] == '1':

                count += 1
            
        

        return count
        