# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # start at root as it's always a common ancestor of p and q
        curr = root 

        while curr:
            # curr smaller than p and q, both nodes are in the right subtree
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right

            # curr larger than p and q, both nodes are in the left subtree
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left

            # otherwise curr is either p, q, or the split point between p and q
            else:
                return curr

            
