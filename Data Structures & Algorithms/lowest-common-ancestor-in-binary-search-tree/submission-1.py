# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # current node we are on
        # start at root because root will always be a common ancester
        curr = root 

        while curr:
            # current smaller than 2 nodes values, move to right subtree to get bigger numbers
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            # current larger than 2 nodes values, move to left subtree to get smaller numbers
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            # current is now at either p or q node or at the lowest common ancester being the value inbetween p and q
            else:
                return curr
                
            
