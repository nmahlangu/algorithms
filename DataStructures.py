# array
l = []
l.append(1)            # add to array
l[0]                   # access element
if 1 in l:    
   print "Contains 1"  # check if contains element

# stack
s = []
s.append(1)            # push an element
s.pop()                # pop an element

# queue
q = [] 
q.append(1)            # enqueue an element
q.pop(0)               # dequeue an element

# priority queue
from Queue import PriorityQueue
pq = PriorityQueue()
pq.put((0,"Nicholas"))  # add an element (first element in tuple is priority)
pq.empty()             # check if empty
pq.qsize()             # get size
pq.get()               # dequeue an element (using priority)

# set
from sets import Set
s = set()
s.add(1)               # add an element
s.remove(1)            # remove an element

