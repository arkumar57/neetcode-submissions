class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        

        for i in range(len(tasks)):

            tasks[i].append(i)
        
        tasks.sort(key = lambda x:x[0])


        res = []

        minheap = []

        i = 0
        time = 0

        while len(res) < len(tasks):

            while i < len(tasks) and tasks[i][0] <= time:

                heapq.heappush(minheap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not minheap:

                time = tasks[i][0]
                continue

            proctime, index = heapq.heappop(minheap)
            time += proctime
            res.append(index)
        

        return res
            



        