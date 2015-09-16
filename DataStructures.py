# array
l = []
l.append(1)             # add to array
l[0]                    # access element
if 1 in l:    
   print "Contains 1"   # check if contains element

# stack
s = []
s.append(1)             # push an element
s.pop()                 # pop an element

# queue
q = [] 
q.append(1)             # enqueue an element
q.pop(0)                # dequeue an element

# priority queue
from Queue import PriorityQueue
pq = PriorityQueue()
pq.put((0,"Nicholas"))  # add an element (first element in tuple is priority)
pq.empty()              # check if empty
pq.qsize()              # get size
pq.get()                # dequeue an element (using priority)

# set
from sets import Set
s = set()
s.add(1)                # add an element
s.remove(1)             # remove an element

# trie
from pytrie import SortedStringTrie as trie
t = trie({'all': 2, 'allot': 3, 'alloy': 4, 'aloe': 5, 'an': 0, 'ant': 1, 'are': 6, 'be': 7}) # arg is a dict
t.keys('al')                           # get keys prefixed by 'al'
t.items('al')                          # get values associated with keys prefixed by 'al'
t.longest_prefix('antonym', None)      # get the longest key that is a prefix of 'antonym'
t.longest_prefix_item('allstar', None) # get the value associated with the longest key that is a prefix of 'allstar'
t.longest_prefix_item('area', None)    # get item ((key,value) tuple) associated with the longest key that is a prefix of 'area'
t.iter_prefixes('al')                  # get iterator over the keys that are prefixes of 'al'
t.iter_prefix_values('al')             # get iterator over the values that are associated with the prefixes of 'al'
t.iter_prefix_items('al')              # get iterator over the items ((key,value) tuples) that are associated with keys that are prefixes of 'al'
