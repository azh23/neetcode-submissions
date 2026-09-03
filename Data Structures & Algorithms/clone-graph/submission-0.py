"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        root = Node(node.val)

        cloned = dict()
        def dfs(node):
            nonlocal cloned
            if node in cloned:
                return cloned[node]

            new_node = Node(node.val)
            cloned[node] = new_node

            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node

        return dfs(node)
        
        