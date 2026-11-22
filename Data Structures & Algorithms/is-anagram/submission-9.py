class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):

            return False
        
        mymap = {}

        for char in s:

            if char not in mymap:

                mymap[char] = 1
            
            else:
                mymap[char] += 1
        
        print(mymap)
        for alphab in t:

            if alphab not in mymap:

                return False
            
            else:
                mymap[alphab] += 1
        
        for item in mymap:

            if mymap[item] % 2 == 0:

                continue
            else:
                return False
        
        return True