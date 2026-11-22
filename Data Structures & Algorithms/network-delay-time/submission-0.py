class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        min_heap = []

        heapq.heapify(min_heap)

        dist = [float('inf')] * (n + 1)

        dist[k] = 0

        heapq.heappush(min_heap, [0, k])
        
        while min_heap:

            d, ind = heapq.heappop(min_heap)

            for node in times:

                if node[0] == ind:
                    edge_weight = node[2]
                    adjnode = node[1]

                    if d + edge_weight < dist[adjnode]:

                        dist[adjnode] = d + edge_weight
                        heapq.heappush(min_heap, [dist[adjnode], adjnode])
        

        if max(dist[1:]) == float('inf'):

            return -1
        else:
            return max(dist[1:])

