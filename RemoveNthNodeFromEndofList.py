# Given a linked list, remove the nth node from the end of list and return its head. 
# For example,
#   Given linked list: 1->2->3->4->5, and n = 2.
#   After removing the second node from the end, the linked list becomes 1->2->3->5.
# Notes:
#   Given n will always be valid.
#   Try to do this in one pass.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        fast = slow = head
        for i in xrange(n):
            fast = fast.next        
        if not fast:
            head = head.next
            return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

# Solution: Use a fast and a slow pointer, where the fast pointer is n steps ahead of the slow
# pointer. When the fast one reaches the end, the slow one will point to the element right
# before the one that needs to be removed.
