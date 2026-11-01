class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)

        count_1 = [0] * 26
        count_2 = [0] * 26

        if n1 > n2:
            return False

        for i in range(n1):

            count_1[ord(s1[i]) - ord("a")] += 1
            count_2[ord(s2[i]) - ord("a")] += 1

        if count_1 == count_2:
            return True
        
        for j in range(n1, n2):
            count_2[ord(s2[j]) - ord("a")] += 1
            count_2[ord(s2[j - n1]) - ord("a")] -=1

            if count_1 == count_2:

                return True
        
        return False

        
        