# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if root is None:
            return

        min_heap = []

        min_heap.append(root.val)

        def dfs(kid):

            if kid is None:
                return

            min_heap.append(kid.val)

            l = dfs(kid.left)
            r = dfs(kid.right)
        

        a = dfs(root.left)
        b = dfs(root.right)

        i = 0

        heapq.heapify(min_heap)
        while i < k - 1:

            heapq.heappop(min_heap)
            i += 1
        
        return heapq.heappop(min_heap)
        