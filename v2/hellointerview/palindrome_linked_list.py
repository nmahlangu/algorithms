class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode):
        # find middle of list
        fast: None | ListNode = head
        slow: None | ListNode = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse 2nd half
        prev: None | ListNode = None
        curr: None | ListNode = slow

        while curr:
            next_: None | ListNode = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        # traverse from front and rear and compare
        left: None | ListNode = head
        right: None | ListNode = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
