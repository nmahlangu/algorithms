# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

from Queue import PriorityQueue

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        queue = PriorityQueue()
        head = tail = ListNode("dummy")
        for i, item in enumerate(lists):
            if item:
                queue.put((item.val,item))
        while not queue.empty():
            elt = queue.get()[1]
            tail.next = elt
            tail = tail.next
            if elt.next:
                queue.put((elt.next.val,elt.next))
        return head.next

# Solution: Throw the head of each list into a Priority Queue. While the queue is not empty,
# pop and append the next element to the tail of the new linked list, making sure to throw it's
# next element into the priority queue when it is taken out. Time complexity is O(nlog(k)) and
# space complexity is O(1) (since it's storing at most k nodes)
