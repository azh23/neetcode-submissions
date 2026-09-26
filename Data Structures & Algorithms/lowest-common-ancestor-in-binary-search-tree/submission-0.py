# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # [has p, has q]
        lca = None
        def traverse(node):
            nonlocal lca
            if not node:
                return [False, False]
            
            left, right = traverse(node.left), traverse(node.right)
            if lca:
                return

            has_p = node.val == p.val or left[0] or right[0]
            has_q = node.val == q.val or left[1] or right[1]
            if has_p and has_q:
                lca = node
            return [has_p, has_q]
        traverse(root)
        return lca
            