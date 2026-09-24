class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        result = ""

        count = 0

        if s == " ":

            return 1
        if len(s) == 0:

            return 0
        
        left = 0
        
        result = s[left]

        count = len(result)

        right = 1

        while right < len(s):

            if s[right] not in result:

                result += s[right]

                count = max(count, len(result))

                right += 1
            
            else:

                index = result.find(s[right])

                left = index + 1

                result = result[left:]

                result += s[right]

                count = max(count, len(result))

                right += 1
        

        return count








        

        


        