# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursion

        # Base Case: leaf
        if not root:
            return None

        # Recursive Step: swap left and right subtree
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursive Step: call the method again on subtree left & right child
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
