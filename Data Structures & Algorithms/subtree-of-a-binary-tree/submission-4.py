# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Recursion

        # Base case: an empty subRoot is always a subtree
        if not subRoot:
            return True

        # Base case: root is empty but subRoot is not, so no match
        if not root:
            return False

        # Current node check: see if the tree starting here matches subRoot
        if self.isSameTree(root, subRoot):
            return True

        # Recursive case: keep searching for the same subRoot in root's subtrees
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, p, q):
        # Recursion

        # Base case: both subtrees are empty, so they match
        if not p and not q:
            return True

        # Base case: only one subtree is empty, so they do not match
        if not p or not q:
            return False

        # Current node check: values must match
        if p.val != q.val:
            return False

        # Recursive case: both left and right subtrees must match
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )