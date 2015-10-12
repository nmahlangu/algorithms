# Implement a class for a linked list that supports printing the list, adding
# to the tail, adding to the head, removing an element, mapping over the list,
# and reducing over it.

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # prints the list
    def print_list(self):
        curr = self.head
        while curr:
            print curr.value,
            curr = curr.next
        print

    # reverses the list
    def reverse_list(self):
        new_head = Node("dummy")
        curr = self.head
        while curr:
            rest = curr.next
            curr.next = new_head.next
            new_head.next = curr
            curr = rest
        self.head = new_head.next

    # adds an element to the end
    def add_to_list_end(self, elt):
        curr = self.head
        if not curr:
            self.head = Node(elt)
        else:
            next = curr.next
            while next:
                curr = next
                next = next.next
            curr.next = Node(elt)

    # removes an element
    def remove_from_list(self, elt):
        if not self.head:
            return
        # head
        if self.head.value == elt:
            self.head = self.head.next
        # in list middle or at tail
        else:
            curr = self.head
            next = self.head.next
            while next:
                if next.value == elt:
                    curr.next = next.next
                    break
                curr = next
                next = next.next            

    # maps a function over each element
    def map(self, f):
        curr = self.head
        while curr:
            curr.value = f(curr.value)
            curr = curr.next

