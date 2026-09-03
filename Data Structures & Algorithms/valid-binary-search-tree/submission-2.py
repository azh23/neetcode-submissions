# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        def traverse(curr, mn, mx):
            nonlocal valid
            if curr is None:
                return
            if curr.val <= mn:
                valid = False
                return
            if curr.val >= mx:
                valid = False
                return
            traverse(curr.left, mn, curr.val)
            traverse(curr.right, curr.val, mx)
            
        traverse(root, -float('inf'), float('inf'))
        return valid
    