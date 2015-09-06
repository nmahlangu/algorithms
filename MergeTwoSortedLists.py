# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing 
# together the nodes of the first two lists.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3_head = l3_tail = ListNode("tmp")
        while l1 and l2:
            if l1.val < l2.val:
                l3_tail.next = l1
                l1 = l1.next
            else:
                l3_tail.next = l2
                l2 = l2.next
            l3_tail = l3_tail.next
        if l1:
            l3_tail.next = l1
        elif l2:
            l3_tail.next = l2
        return l3_head.next

# Solution: Repeatedly take the smaller element of the head of both linked lists.
# Once one is gone, attach the rest of the other one.