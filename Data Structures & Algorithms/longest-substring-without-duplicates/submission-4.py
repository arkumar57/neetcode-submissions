class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:

            return 1
        
        if len(s) == 0:

            return 0


        l = 0

        myset = set()

        result = 0

        i = 1

        myset.add(s[l])

        count = 1

        for i in range(1, len(s)):

            while s[i] in myset:

                myset.remove(s[l])
                l += 1
                
            myset.add(s[i])
        
            count = max(count, i - l + 1)
        

        return count




        

        


        