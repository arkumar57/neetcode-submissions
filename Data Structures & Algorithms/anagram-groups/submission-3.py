class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mymap = defaultdict(list)

        for stri in strs:

            li = [0] * 26

            for alpha in stri:

                li[ord(alpha) - ord("a")] += 1
            
            # if tuple(li) not in mymap:

            #     mymap[tuple(li)] = stri
            
            # else:
            #     mymap[tuple(li)].append(stri)

            mymap[tuple(li)].append(stri)
        
        return list(mymap.values())

