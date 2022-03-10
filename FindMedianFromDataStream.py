# Given a stream of integers, create a data structure that can efficiently store and compute the median of
# all integers seen so far.

import heapq

class MedianFinder:
    '''
    Invariant: size of max heap and min heap can differ at most by 1

    There exists no max heap implementation in python's heapq library. A workaround
    for this is to negate numbers upon adding or removal from the heap when using
    the heapq library.  
    '''
    
    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []
        
    def insert(self, elt: int) -> None:
        if len(self.right_min_heap) == 0 or elt > self.right_min_heap[0]:
            heapq.heappush(self.right_min_heap, elt)
        else:
            heapq.heappush(self.left_max_heap, elt * -1)
                
        diff = len(self.left_max_heap) - len(self.right_min_heap)
        if abs(diff) < 2:
            return
        
        if diff > 0:
            popped = heapq.heappop(self.left_max_heap) * -1
            heapq.heappush(self.right_min_heap, popped)
        else:
            popped = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, popped * -1)
        
        return
        
    def get_median(self) -> float:       
        if len(self.left_max_heap) > len(self.right_min_heap):
            return self.left_max_heap[0] * -1
        elif len(self.left_max_heap) < len(self.right_min_heap):
            return self.right_min_heap[0]
        else:
            return ((self.left_max_heap[0] * -1) + self.right_min_heap[0]) / 2

# Tests
nums = iter([1,4,2,7,4,3,8,9])
m = MedianFinder()

m.insert(next(nums))
m.insert(next(nums))
m.insert(next(nums))
assert m.get_median() == 2

m.insert(next(nums))
m.insert(next(nums))
m.insert(next(nums))
assert m.get_median() == 3.5

m.insert(next(nums))
m.insert(next(nums))
assert m.get_median() == 4

# Time complexity
# - insert: O(log(n))
# - get_median: O(1)
#
# Space Complexity: O(n)