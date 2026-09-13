# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def sameTree(root, newRoot):
            if not root and not newRoot:
                return True
            if root and newRoot and root.val == newRoot.val:
                return sameTree(root.left, newRoot.left) and sameTree(root.right, newRoot.right)
            return False

        def traverse(node):
            if not node:
                return False
            if sameTree(node, subRoot):
                return True
            return traverse(node.left) or traverse(node.right)

        return traverse(root)