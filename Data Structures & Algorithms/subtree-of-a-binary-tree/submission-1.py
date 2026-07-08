# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Recursion
        # Base Case: subtree is empty, so must be part of tree
        if not subRoot: return True

        # Base Case: tree empty, so can't be part of tree
        if not root: return False

        # Current Node Check: found matching root nodes and left and right subtrees
        if self.isSameTree(root, subRoot): return True

        # Recursive Case: check left and right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        # Recursion
        # Base Case: both tree/subtree empty, so match
        if not p and not q: return True

        # Base Case: one tree/subtree empty, other tree/subtree not empty, so no match
        if not p or not q: return False

        # Current Node Check:
        if p.val != q.val: return False

        # Recursively check left and right subtree of current node
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)