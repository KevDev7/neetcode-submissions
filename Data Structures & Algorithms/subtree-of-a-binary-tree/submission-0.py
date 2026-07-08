# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Empty subRoot is always considered a subtree
        if not subRoot:
            return True

        # If root is empty but subRoot is not, subRoot cannot exist here
        if not root:
            return False

        # If the trees starting at root and subRoot are the same, we found the subtree
        if self.isSameTree(root, subRoot):
            return True

        # Otherwise, keep searching in the left and right subtrees
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, p, q):
        # Both subtrees are empty, so they match
        if not p and not q:
            return True

        # Only one subtree is empty, so they do not match
        if not p or not q:
            return False

        # Current node values must match
        if p.val != q.val:
            return False

        # Both left and right subtrees must match
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )