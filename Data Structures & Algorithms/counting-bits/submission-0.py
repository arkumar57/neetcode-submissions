class Solution:
    def countBits(self, n: int) -> List[int]:

        mylist = []

        for i in range(0, n+1):

            mylist.append(bin(i))
        

        mycount = []

        for i in mylist:

            count = 0;

            for m in range(2, len(i)):

                if i[m] == "1":

                    count += 1;
                
                else:

                    continue
            mycount.append(count)
        

        return mycount










        
        