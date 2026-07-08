# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case: empty subtree always exist in main tree
        if not subRoot:
            return True
        
        # Base Case: non-existent main tree cannot contain any subtree
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        # Recursive Step
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    

    def isSameTree(self, p, q):
        # Base Case: both tree/subtree empty
        if not p and not q:
            return True
        # Base Case: only one tree/subtree empty
        if not p or not q:
            return False
        
        # Current Node Check
        if p.val != q.val:
            return False
        
        # Recursive Step
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)