class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode):
        seen: set[ListNode] = set()
        curr: ListNode = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False
