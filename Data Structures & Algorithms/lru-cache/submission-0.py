class Node:
    def __init__(self, key, val, ):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        # dummy nodes
        self.begin = Node(0,0)
        self.end = Node(0,0)
        self.begin.next = self.end
        self.end.prev = self.begin

    def remove_node(self, node):
        prv = node.prev
        prv.next = node.next
        node.next.prev = prv

    def insert_node(self, node):
        self.end.prev.next = node
        node.prev = self.end.prev
        self.end.prev = node
        node.next = self.end

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.insert_node(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.begin.next
            self.remove_node(lru)
            del self.cache[lru.key]
        
