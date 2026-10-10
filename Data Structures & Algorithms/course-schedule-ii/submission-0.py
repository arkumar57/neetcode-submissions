class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = defaultdict(list)

        indegree = [0] * numCourses

        for src,dst in prerequisites:

            adj_list[src].append(dst)

            indegree[dst] += 1
        

        q = deque()
        result = []

        for i in range(numCourses):

            if indegree[i] == 0:

                q.append(i)

                result.append(i)
        
        finish = 0

        while q:

            node = q.popleft()
            finish += 1

            for nei in adj_list[node]:

                indegree[nei] -= 1

                if indegree[nei] == 0:

                    q.append(nei)
                    result.append(nei)

        
        empty_array = []

        if finish == numCourses:

            return result[::-1]
        
        else:

            return empty_array
        
        return new_result


        