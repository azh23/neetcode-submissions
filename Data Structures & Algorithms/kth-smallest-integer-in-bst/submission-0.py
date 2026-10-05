# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        i = 1
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if i == k:
                return current.val
            i += 1

            current = current.right
