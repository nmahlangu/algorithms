# You are given two linked lists representing two non-negative numbers. The digits are stored 
# in reverse order and each of their nodes contain a single digit. Add the two numbers and 
# return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
            
    def addTwoNumbers(self, l1, l2):
        p1,p2 = l1,l2
        head = None
        p3 = head
        carry = 0
        
        while p1 or p2:
            if p1:
                carry += p1.val
                p1 = p1.next
            if p2:
                carry += p2.val
                p2 = p2.next
                
            if not head:
                head = ListNode(carry%10)
                p3 = head
            else:
                p3.next = ListNode(carry%10)
                p3 = p3.next
            carry /= 10
        
        if carry == 1:
            p3.next = ListNode(carry)
            p3 = p3.next
            
        return head

# Solution:
# Build the linked list (from head to tail) one number at a time, making 
# sure to account for the carry for each number and after building the whole
# list.