# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            # Base case: use "N" to mark an empty child
            if not node:
                result.append("N")
                return

            # Preorder: save current node first
            result.append(str(node.val))

            # Then save the left subtree
            dfs(node.left)

            # Then save the right subtree
            dfs(node.right)
        
        dfs(root)
        
        # Turn the list into one string
        return ",".join(result)

        
    # Decodes your encoded data back into a tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0  # Current index in values

        def dfs():
            # Base case: "N" means this child is empty
            if values[self.i] == "N":
                self.i += 1
                return None

            # Preorder: create the current node first
            node = TreeNode(int(values[self.i]))
            self.i += 1

            # Rebuild the left subtree
            node.left = dfs()

            # Rebuild the right subtree
            node.right = dfs()

            # Return the rebuilt node/subtree
            return node

        return dfs()
