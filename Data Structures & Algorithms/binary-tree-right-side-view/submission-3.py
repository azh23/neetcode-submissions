# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root: q.append(root)
        res = []

        while q:
            ct = len(q)
            to_add = None
            for _ in range(ct):
                curr = q.popleft()
                if not to_add:
                    to_add = curr.val
                if curr.right: q.append(curr.right)
                if curr.left: q.append(curr.left)
            res.append(to_add)
        return res