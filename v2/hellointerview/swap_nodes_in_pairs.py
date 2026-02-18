import unittest


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode):
        if not head:
            return None

        dummy_node: ListNode = ListNode()
        dummy_node.next = head
        a: ListNode = dummy_node
        b: ListNode = head
        c: None | ListNode = head.next

        while c:
            d: None | ListNode = c.next
            a.next = c
            c.next = b
            b.next = d

            a = b
            b = d
            c = d.next if d else None

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
            Solution().swapPairs(Solution().array_to_list([5, 4, 3, 2, 1]))
        )
        self.assertEqual([4, 5, 2, 3, 1], actual)

    def test_example2(self):
        actual = Solution().list_to_array(
            Solution().swapPairs(Solution().array_to_list([4, 3, 2, 1]))
        )
        self.assertEqual([3, 4, 1, 2], actual)


if __name__ == "__main__":
    unittest.main()
