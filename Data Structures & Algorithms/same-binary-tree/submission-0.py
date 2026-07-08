# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursion
        # Base Case: both trees are empty, so they match
        if not p and not q:
            return True

        # Base Case: one tree empty, other tree not empty, so they do not match
        elif not p or not q:
            return False

        # Current Node check
        elif p.val != q.val:
            return False

        # Recursive Case: recursively call isSameTree to check left and right subtree
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )