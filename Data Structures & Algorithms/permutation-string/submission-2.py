class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        if len(s1) > len(s2):

            return False

        char_count = [0] * 26

        for char in s1:

            char_count[ord(char) - ord("a")] += 1
        
        l = 0

        r = len(s1)

        while r <= len(s2):

            print(r)
            char_check = [0] * 26
            for char in range(l, r):
                char_check[ord(s2[char]) - ord("a")] += 1
            
            if char_check == char_count:

                return True
            else:

                r += 1
                l += 1
        

        return False



