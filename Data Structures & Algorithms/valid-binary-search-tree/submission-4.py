# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(curr, mn, mx):
            if curr is None:
                return True
            if curr.val <= mn:
                return False
            if curr.val >= mx:
                return False
            return traverse(curr.left, mn, curr.val) and traverse(curr.right, curr.val, mx)
            
        return traverse(root, -float('inf'), float('inf'))
    