class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        if len(s1) > len(s2):

            return False

        char_count = [0] * 26

        for char in s1:

            char_count[ord(char) - ord("a")] += 1
        
        l = 0

        r = len(s1)

        char_check = [0] * 26

        for char in range(l, r):

            char_check[ord(s2[char]) - ord("a")] += 1

        if char_check == char_count:

            return True

        while r < len(s2):

            r += 1
            char_check[ord(s2[r - 1]) - ord("a")] += 1
            char_check[ord(s2[l]) - ord("a")] -= 1
            l += 1

            if char_check == char_count:

                return True

        return False



