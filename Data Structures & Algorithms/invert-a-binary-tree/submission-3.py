# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursion

        # Base case: if this subtree is empty, stop recursion
        if not root:
            return None

        # Current node work: swap current node's left and right subtrees
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursive case: invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root