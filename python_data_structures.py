############
# Variables
############
elts = [1,5,4,2,3]


#################################
# List Stack
# https://docs.python.org/2/tutorial/datastructures.html
#################################
stack = []

# push
# [1,5,4,2,3]
for e in elts:
	stack.append(e)

# pop 
# 3,2,4,5,1
for i in range(len(stack)):
	stack.pop()     


#################################
# List Queue
# https://docs.python.org/2/tutorial/datastructures.html
#################################
from collections import deque
queue = deque([])

# enqueue
# [1,5,4,2,3]
for e in elts:
	queue.append(e) 

# dequeue  
# 1,5,4,2,3 
queue.popleft()


#################################
# Queue
# https://docs.python.org/2/library/queue.html#module-Queue
#################################
import Queue
queue = Queue.Queue()

# enqueue
# [1,5,4,2,3]
for e in elts:
	queue.put(e)  

# dequeue
# 1,5,4,2,3
for i in range(len(elts)):      
	queue.get()         

queue.qsize()      # returns the approximate size of the queue
queue.empty()      # returns True if empty, False if not
queue.full()	   # returns True if full, False if not


#################################
# Priority Queue
# https://docs.python.org/2/library/queue.html#Queue.PriorityQueue
#################################
import Queue
pqueue = Queue.PriorityQueue()

# enqueue (with priority)
for e in elts:
	pqueue.put(e)     

# dequeue (with priority)
# 1,2,3,4,5
for i in range(len(elts)):
	pqueue.get()    

pqueue.qsize()      # returns the approximate size of the queue
pqueue.empty()      # returns True if empty, False if not
pqueue.full()	    # returns True if full, False if not


#################################
# Min-Heap
# https://docs.python.org/2/library/heapq.html
#################################
import heapq
h = []

# transform list into a heap, in-place, in linear 
# time
# [1,2,4,5,3]
heapq.heapify([1,5,4,2,3]) 

# push item onto heap, maintaining heap invariant
# [1,2,4,5,3]
for e in elts:
	heapq.heappush(h,e) 

# pop and return smallest item from heap, maintaining 
# the heap invariant.
# 1,2,3,4,5
for i in range(len(elts)):
	heapq.heappop(h) 

