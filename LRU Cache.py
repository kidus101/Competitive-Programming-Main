class Node:
        def __init__(self, key, value):
            self.value = value
            self.key = key
            self.prev = None
            self.next = None
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        
    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
            
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DLL()
        self.cache = {}
        
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].value
            self.dll.delete(self.cache[key])
            node = Node(key, value)
            self.dll.insert(node)
            self.cache[key] = node
            return value
        return (-1)        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.dll.delete(self.cache[key])
        elif len(self.cache) >= self.capacity:
            del self.cache[self.dll.head.key]
            self.dll.delete(self.dll.head)
        node = Node(key, value)
        self.dll.insert(node)
        self.cache[key] = node
        
        # Time:O(1)
        # Space:O(n)
      
