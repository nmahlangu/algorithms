import hashlib
import bisect


class ConsistentHashRing:
    def __init__(self, nodes=None, replicas=100):
        """
        Initialize the hash ring.
        :param nodes: list of node identifiers (e.g. IPs or server names)
        :param replicas: number of virtual nodes per physical node
        """
        self.replicas = replicas
        self.ring = dict()
        self.sorted_keys = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        """Return a hash value using SHA-256."""
        h = hashlib.sha256(key.encode('utf-8')).hexdigest()
        return int(h, 16)

    def add_node(self, node):
        """Add a node with virtual nodes."""
        for i in range(self.replicas):
            virtual_node_id = f"{node}#{i}"
            key = self._hash(virtual_node_id)
            self.ring[key] = node
            bisect.insort(self.sorted_keys, key)

    def remove_node(self, node):
        """Remove a node and its virtual nodes."""
        for i in range(self.replicas):
            virtual_node_id = f"{node}#{i}"
            key = self._hash(virtual_node_id)
            if key in self.ring:
                del self.ring[key]
                index = bisect.bisect_left(self.sorted_keys, key)
                if index < len(self.sorted_keys) and self.sorted_keys[index] == key:
                    self.sorted_keys.pop(index)

    def get_node(self, key):
        """Get the node responsible for a given key."""
        if not self.ring:
            return None

        key_hash = self._hash(key)
        index = bisect.bisect(self.sorted_keys, key_hash) % len(self.sorted_keys)
        return self.ring[self.sorted_keys[index]]


# Example usage
if __name__ == "__main__":
    nodes = ['node1', 'node2', 'node3']
    ring = ConsistentHashRing(nodes, replicas=100)

    keys = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    for key in keys:
        print(f"{key} is mapped to {ring.get_node(key)}")

    print("\nRemoving node2...")
    ring.remove_node('node2')

    for key in keys:
        print(f"{key} is now mapped to {ring.get_node(key)}")