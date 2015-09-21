# You're given an address book which contains a list of contacts combined
# from different sources. Each contact has 1 or more email addresses.
# Your job is to write a function that groups together all contacts which
# share any email together.

from sets import Set

class Contact:
    def __init__ (self, emails):
        self.emails = emails

def dfs(email_dict, contact, seen):
    found = []
    queue = [contact]
    while queue:
        node = queue.pop()
        if node not in seen:
            seen.add(node)
            found.append(node)
            for email in node.emails:
                for other in email_dict[email]:
                    queue.append(other)
        seen.add(contact)
    return found
            
def deduplicate(contacts):
    if not contacts:
        return []
    email_dict = {}
    for contact in contacts:
        for email in contact.emails:   
            email_dict.setdefault(email,[])
            email_dict[email].append(contact)
    seen = set()
    return filter(None, [dfs(email_dict, contact, seen) for contact in contacts])

# Good solution: Consider each contact a node and an edge exists between 2 nodes
# if they share at least 1 email. Using this representation, each connected component
# will be 1 group. Implementation-wise, run DFS from every node, making sure to keep
# track of any element that's been seen so far. Because DFS will return None if the
# root has been seen, filter out empty groups. Time complexity is O(v+e), where 'v' is
# the number of nodes and 'e' is the number of edges.

class Node():
    def __init__ (self, value):
        self.value = value
        self.parent = self  
        self.rank = 0

    # path compression
    def find(self):
        if self.parent != self:
            self.parent = self.parent.find()
        return self.parent
    
    def union(self, node):
        root = self.find()
        other_root = node.find()

        # union by rank
        if root.rank < other_root.rank:
            root.parent = other_root
        else:
            other_root.parent = root
            if root.rank == other_root.rank:
                root.rank += 1

def deduplicate(contacts):
    email_dict = {}
    nodes = []
    for contact in contacts:
        node = Node(contact)
        nodes.append(node)
        for email in contact.emails:
            if email in email_dict:
                seen_node = email_dict[email]
                seen_node.union(node)
            else:
                email_dict[email] = node
    
    # return disjoint sets as a list
    result = {}
    for node in nodes:
        parent = node.find()
        result.setdefault(parent,[])
        result[parent].append(node.value)
    return result.values()

# Best solution: Use a disjoint-set data structure with union by rank and path compression.
# Time complexity is amortized O(v), where 'v' is the total number of emails in all contacts.
#
# Notes: In this data structure, each set is represented by a tree, so that each element points
# to a parent in the tree. Furthermore, the root of the tree will point to itself. To keep
# trees short, we two heuristics known as union by rank and path compression. In union by rank,
# each element initially has a rank of 0. When 2 elements are unioned together (call them A and B),
# one of two things happens: if they have the same rank, point B's root's parent pointer at A and
# increment A's rank by 1; if they have different rank, point the shorter one's root's parent pointer
# at the longer one's root. In path compression, the idea is that once we perform a find on some
# element, we should adjust its parent pointer so that it points directly to the root. That way, if
# we ever do another find on it, we start out much closer to the root.
