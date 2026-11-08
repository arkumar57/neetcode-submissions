class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s is None:
            return 1

        right = 0
        myset = set()
        left = 0
        result = 0
        while right < len(s):

            if s[right] not in myset:

                myset.add(s[right])
                right += 1
                result = max(result,right - left)
            else:

                result = max(result,right - left)

                while s[right] in myset and left < right:

                    myset.remove(s[left])
                    left += 1
                myset.add(s[right])
                right += 1
        
        return result

