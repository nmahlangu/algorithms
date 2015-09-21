from sets import Set

class Contact:
    def __init__ (self, emails, name):
        self.emails = emails
        self.name   = name

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


def run_test():
    c1 = Contact(["shuw@fb.com", "shu@gmail.com"], "c1")
    c2 = Contact(["bob@fb.com"], "c2")
    c3 = Contact(["shu@gmail.com", "shuwu@yahoo.com"], "c3")
    c4 = Contact(["shuwu@yahoo.com"], "c4")
    c5 = Contact(["bob@fb.com"], "c5")
    c6 = Contact(["jamie@fb.com"], "c6")
    contacts = [c1,c2,c3,c4,c5,c6]
    deduplicate(contacts)

    res = deduplicate(contacts)
    for i, item in enumerate(res):
        print "Group %d: " % (i+1)
        for person in item:
            print person.name
        print
run_test()

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

run_test()
