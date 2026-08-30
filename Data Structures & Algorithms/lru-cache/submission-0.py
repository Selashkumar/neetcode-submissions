class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.catch = {}
        self.lru, self.mru = Node(0, 0), Node(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node
    def get(self, key: int) -> int:
        if key in self.catch:
            self.remove(self.catch[key])
            self.insert(self.catch[key])
            return self.catch[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.catch:
            self.remove(self.catch[key])
        self.catch[key] = Node(key, value)
        self.insert(self.catch[key])
        if len(self.catch) > self.cap:
            lru = self.lru.next
            self.remove(lru)
            del self.catch[lru.key]