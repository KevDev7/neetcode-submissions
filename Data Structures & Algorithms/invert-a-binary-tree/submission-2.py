# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursion

        # Base Case: no children nodes, return none
        if not root:
            return None

        # Swap left and right subtrees
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursive Case: recursively call invertTree again for left & right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root