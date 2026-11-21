class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)

        maxHeap = [cnt for cnt in count.values()]

        heapq.heapify_max(maxHeap)

        cycles = 0

        while maxHeap:

            temp = []
            for i in range(n + 1):
                
                if maxHeap:

                    temp.append(heapq.heappop_max(maxHeap))

            for i in temp:

                if (i - 1 > 0):

                    heapq.heappush_max(maxHeap, i - 1)
            
            if not maxHeap:

                cycles += len(temp)
            
            else:
                cycles += n+1
        

        return cycles
                
