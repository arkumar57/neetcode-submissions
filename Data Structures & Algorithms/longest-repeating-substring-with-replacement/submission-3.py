class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        result = 0

        myset = set(s)

        for i in myset:

            left = 0
            mismatches = 0

            for r in range(len(s)):

                if s[r] != i:

                    mismatches += 1
                
                while mismatches > k:
                    if s[left] != i:
                        mismatches -= 1
                    left += 1
                
                result = max(result, r - left + 1)
        
        return result
            


        



        






        
        