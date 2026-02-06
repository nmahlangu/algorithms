import unittest


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode):
        # find middle of list
        fast: None | ListNode = head
        slow: None | ListNode = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half of list
        second_half = slow.next
        slow.next = None
        curr: None | ListNode = second_half
        prev: None | ListNode = None
        while curr:
            next_: None | ListNode = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        # merge both lists
        dummy_node: ListNode = ListNode()
        l1: None | ListNode = head
        l2: None | ListNode = prev
        l3: ListNode = dummy_node

        while l1 and l2:
            l3.next = l1
            l3 = l3.next
            l1 = l1.next

            l3.next = l2
            l3 = l3.next
            l2 = l2.next

        if l1:
            l3.next = l1
        elif l2:
            l3.next = l2

        return dummy_node.next

    def list_to_array(self, head: ListNode) -> list[int]:
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result

    def array_to_list(self, arr: list[int]) -> ListNode | None:
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().list_to_array(
            Solution().reorderList(Solution().array_to_list([2, 8, 5, 6, 2, 3]))
        )
        self.assertEqual([2, 3, 8, 2, 5, 6], actual)


if __name__ == "__main__":
    unittest.main()
