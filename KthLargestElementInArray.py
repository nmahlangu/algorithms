# Write a function that takes an array and returns the kth smallest
# element in that array. Raise an exception if the inputs are invalid.

from Queue import PriorityQueue

def get_kth_largest(arr,k):
    if not arr or k > len(arr):
        raise Exception("Invalid input")

    pqueue = PriorityQueue()
    for elt in arr:
        pqueue.put(elt)

    for i in xrange(k):
        result = pqueue.get()
    return result

# Solution: Throw each element into a Priority Queue (can be implemented
# as a min-heap) and dequeue from it k times. Return the element that is
# dequeued the kth time. Time complexity is O(n + klog(n)), since you're
# doing n O(1) inserts into the Priority Queue and then doing k get min
# operations which each take O(log(n)), and space complexity is O(n).
# 
# Note: if this question asked for the kth largest element, just insert
# the negated elements into the priority queue and then return the
# negated kth element.
