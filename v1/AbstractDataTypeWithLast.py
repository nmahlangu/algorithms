# Implement the following interface:
#   interface AbstractDataTypeWithLast <K, V> {
#     void put(K k, V v);
#     V    get(K k);
#     void delete(K k);
#     K    last();        // returns last-accessed, non-delete key
#
# Example:
#   put("a", 1)
#   put("b", 2)
#   get("a")  => 1
#   last()    => "a"
#   delete("a")
#   last()    => "b"

class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class ADTWL:
    def __init__(self):
        self.head = None
        self.map = {}

    def move_to_head(self, node):
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def put(self, k, v):
        if k not in self.map:
            node = Node(k,v)
            self.map[k] = node
            self.move_to_head(node)
    
    def get(self, k):
        if k in self.map:
            node = self.map[k] 
            if node == self.head:
                return node.val
            else:
                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                node.prev = None
                self.move_to_head(node)
                return node.val
        return None

    def delete(self, k):
        if k in self.map:
            node = self.map[k]
            if node == self.head:
                if node.next:
                    node.next.prev = None
                    self.head = node.next
                else:
                    self.head = None
            else:
                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev            

    def last(self):
        return self.head.key if self.head else None

# Solution: This problem is asking you to implement an LRU cache. This can
# be done with a double linked list where each node is hashed for O(1) access. 
# put() creates a new node with the key and value if it's not already there and
# places it at the head of the listed. get() returns the value of the key passed
# in and moves the node to the head of the list. delete() deletes the node with
# the corresponding key in the double linked list. last() returns the key of 
# the node at the head of the list.
