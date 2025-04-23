# Implement a binary heap. For the implementation, keep the tree balanced
# by creating a complete binary tree (a tree in which each level has all
# of its nodes, the exception being the bottom level of the tree, which
# is filled in from left to right). 
# 
# Hint: this tree can be represented as a list instead of a data structure 
# with nodes and pointers.

class BinHeap:
    def __init__(self):
        self.heapList = [0]   # zero makes integer division easier
        self.currentSize = 0

    # given a list of integers, starts halfway in the list and
    # percolates each element down into the correct position.
    # Note: all nodes past halfway point will be leaves
    def buildHeap(self,alist):
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        i = len(alist) / 2
        while i > 0:
            self.percDown(i)
            i = i - 1        

    # inserts an element at the end of the list
    # and percolates it up to the correct position
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    # percolates an element up the tree by repeatedly swapping
    # it with its parents until node is in a position where
    # it is greater than both children
    def percUp(self,i):
        while i / 2 > 0:
            if self.heapList[i] < self.heapList[i/2]:
                tmp = self.heapList[i/2]
                self.heapList[i/2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i / 2

    # returns the min element, places the last element at the
    # root, then percolates it down until in correct position
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList.pop()
        self.currentSize -= 1
        self.percDown(1)
        return retval

    # percolates a node down the tree by repeatedly swapping
    # it with its lowest child until node is in a position 
    # where it is less than both children
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    # returns the index of a node's smallest child
    def minChild(self, i):
        if (i * 2) + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[(i*2)+1]:
                return i * 2
            else:
                return i * 2 + 1

# Solution: Use a list where the left child of the parent (p) is at 2p
# and the right child is at 2p+1. Furthermore, maintain the invariant
# that for every node x with parent p, the key in p is smaller than
# or equal to the key in x. 
