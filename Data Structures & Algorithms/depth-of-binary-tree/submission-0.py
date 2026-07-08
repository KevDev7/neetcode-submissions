# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursion

        # Base case: if this subtree is empty, its depth is 0
        if not root:
            return 0

        # Recursive case: get the max depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Add 1 for the current node, then take the deeper subtree
        return 1 + max(left_depth, right_depth)
