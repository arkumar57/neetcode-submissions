# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # if root is None:

        #     return 0

        # queue = deque()

        # queue.append(root)

        # level = 0
        
        # while queue:
            
        #     size = len(queue)
        #     for i in range(size):

        #         node = queue.popleft()

        #         if node.left:
        #             queue.append(root.left)
        #         if node.right:
        #             queue.append(root.right)
            
        #     level += 1
        

        # return level
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
        
        