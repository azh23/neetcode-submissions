# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(node, depth):
            if node is None:
                return depth
            else:
                return max(
                    traverse(node.left, depth + 1), 
                    traverse(node.right, depth + 1))
        return traverse(root, 0)
        