# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = -float('inf')
        def traverse(node):
            nonlocal mx
            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            max_path = node.val + (left if left > 0 else 0) + (right if right > 0 else 0)
            mx = max(mx, max_path)

            return node.val + max(right, left, 0)
        traverse(root)
        return mx
