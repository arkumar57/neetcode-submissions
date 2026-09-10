# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, root: Optional[TreeNode]) -> int:

        if root is None:

            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        return max(left, right) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:

            return True

        
        if abs(self.height(root.left) - self.height(root.right)) > 1:

            return False
        

        return self.isBalanced(root.left) & self.isBalanced(root.right)
        
