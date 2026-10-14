class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        currgas= 0
        n = len(gas)
        startindex = 0


        for i in range(n):
            currgas = currgas + gas[i] - cost[i]

            if currgas < 0:

                currgas = 0
                startindex = i + 1
        

        currgas = 0

        for i in range(n):

            #circular index
            idx = (i + startindex) % n
            currgas = currgas + gas[idx] - cost[idx]

            if currgas < 0:
                return -1
        

        return startindex






        
        