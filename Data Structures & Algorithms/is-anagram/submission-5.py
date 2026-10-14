class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        mymap = {}

        for i in s:

            if i not in mymap:

                mymap[i] = 1
            
            else:
                mymap[i] += 1
        

        for j in t:

            if j not in mymap:
                return False
            else:

                mymap[j] += 1
        
        for key in mymap.keys():

            if mymap[key] % 2 == 0:

                continue
            else:
                return False
        
        return True


        