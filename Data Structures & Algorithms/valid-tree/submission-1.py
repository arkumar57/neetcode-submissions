class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjacency_list = defaultdict(list)

        #n == 0?

        if not n:

            return True

        for edge in edges:

            adjacency_list[edge[0]].append(edge[1])

            adjacency_list[edge[1]].append(edge[0])
        

        visited = set()
        

        def dfs(i, prev):

            if i in visited:

                return False

            visited.add(i)
            for nei in adjacency_list[i]:

                if nei == prev:
                    continue

                if not dfs(nei, i):

                    return False
            
            return True
        

        return dfs(0, -1) and n == len(visited)



        