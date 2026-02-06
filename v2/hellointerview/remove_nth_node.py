class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        slow: None | ListNode = head
        fast: None | ListNode = head
        for _ in range(n):
            fast = fast.next

        if fast is None:
            return slow.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
