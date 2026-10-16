# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encode = []

        def traverse(node):
            nonlocal encode
            if node is None:
                encode.append("N")
                return
            encode.append(str(node.val))
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return ",".join(encode)
        
        #1,2,N,N,3,4,5,N,N,N,N
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        idx = -1
        head = None
        #print(data)
        data = data.split(",")
        #print(data)

        # 0
        # node 1
        def traverse():
            nonlocal idx, head
            idx += 1
            if data[idx] == "N" or not data[idx]:
                return
            #print(data[idx])
            node = TreeNode(int(data[idx]))
            if not head:
                head = node
            node.left = traverse()
            node.right = traverse()
            return node
        
        traverse()
        return head
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
"""