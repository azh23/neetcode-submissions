# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encode = ""

        def traverse(node):
            nonlocal encode
            if node is None:
                encode += "N,"
                return
            encode += str(node.val) + ","
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return encode
        
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