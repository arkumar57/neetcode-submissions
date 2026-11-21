import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []

        for point in points:

            a = math.sqrt((point[0] * point[0]) + (point[1] * point[1]))

            res.append([a, point[0], point[1]])
        
        heapq.heapify(res)

        i = 0

        final = []

        while i < k:
            dis, a, b = heapq.heappop(res)
            final.append([a, b])
            i += 1
        
        return final

            