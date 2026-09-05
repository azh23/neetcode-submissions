# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node):
            nonlocal res
            if node is None:
                return 0 
            left, right = traverse(node.left), traverse(node.right)
            res = max(res, left + right)
            return max(left,right) + 1
        traverse(root)
        return res