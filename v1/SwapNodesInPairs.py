# Given a linked list, swap every two adjacent nodes and return its head.
# For example,
#   Given 1->2->3->4, you should return the list as 2->1->4->3
# Your algorithm should use only constant space. You may not modify the values 
# in the list, only nodes itself can be changed.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = p1 = ListNode("dummy")
        dummy.next = head
        while p1.next and p1.next.next:
            # track first node
            t1 = p1
            p1 = p1.next
            t1.next = p1.next
    
            # track node after pair
            t2 = p1.next.next
            p1.next.next = p1
            p1.next = t2
        return dummy.next

# Solution: Store the first node and update it's pointer to the 3rd node. Then store the node 
# after the pair (4th node) and update the previous node's (3rd node) pointer to the node 
# previous that (2nd node). Then update that node's (2nd node) next pointer to the 2nd store 
# node (4th node). Time complexity is O(n) and space complexity is O(1)
