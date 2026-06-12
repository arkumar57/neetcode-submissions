# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, node):
        if node == None:

            return 0

        else:

            return max(self.height(node.left), self.height(node.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None:

            return True
        
        h_left = self.height(root.left)
        h_right = self.height(root.right)

        if abs(h_left - h_right) > 1:

            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)



        