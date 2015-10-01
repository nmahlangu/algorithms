# Given a list of n elements, return k random elements where
# each one has an equal chance of being selected.

import numpy.random as random

def pick_k_random_items(arr,k):
    if k > len(arr):
        return -1 
    elif k == len(arr):
        return arr

    n = len(arr)
    for i in xrange(len(arr)):
        picked = int(((n - i) * random.random())) + i
        arr[i],arr[picked] = arr[picked],arr[i]
    print arr
    return arr[:k]

# Solution: This solution assumes all the elements are given to you
# in an array and are not streaming. Generate a random index k times 
# between i and n - 1, where i is your counter, and swap that element 
# with the ith element. Return the first k elements of the array. Time
# complexity is O(k).

import numpy.random as random
from Queue import PriorityQueue

def pick_k_random_items(arr,k):
    if k > len(arr):    
        return -1
    elif k == len(arr):
        return arr

    pqueue = PriorityQueue()
    for i in xrange(len(arr)):
        weight = random.random()
        pqueue.put((weight,arr[i]))

    result = [pqueue.get()[1] for i in xrange(k)]
    return result

# Solution: This solution assumes the elements are streaming, e.g.
# that you don't have all of them in memory yet. Generate a random
# weight for each element and insert it into a priority queue
# with that weight. Then pop from the priority queue k times and
# return those elements. Time complexity is O(nlog(k)) if priority 
# queue is a binary heap where insert is O(log(k)), and space complexity
# is O(k).

    
