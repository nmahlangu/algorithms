# Given k sorted arrays (a list of lists), return one sorted array containing all
# elements from all arrays. Assume the longest elements contains n elements.

from Queue import PriorityQueue

def merge(lists):
    # error checking
    if not lists:
        return []
    lists = filter(lambda x: x != [],lists)

    # initialize priority queue
    pqueue = PriorityQueue()
    for lst in lists:
        if lst:
            pqueue.put((lst[0],lst[1:]))
    
    # merge the arrays
    result = []
    while not pqueue.empty():
        elt = pqueue.get()
        num,rest = elt[0],elt[1]
        result.append(num)
        if rest:
            pqueue.put((rest[0],rest[1:]))
    return result

# Create a priority queue that stores tuples of the form (num,rest), where
# num is the first number of a list and rest is the rest of the list. Insert
# a tuple of this form for each list into the priority queue. Repeatedly pop
# the minimum tuple from the priority queue and 1) append the tuple's num
# to the resulting array 2) if rest is not an empty array, insert a new
# tuple into the priority queue containing the next element in the list
# and the rest of that list (without that first element). If priority queue 
# is implemented as a fibonacci heap, time complexity is O(nklog(k)), since doing 
# O(nk) deleteMins() from the priority queue, each of which takes O(log(k)); 
# space complexity is
# O(k), since priority queue will contain at most k elements.
