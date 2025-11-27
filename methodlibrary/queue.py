"""
Name: Mason Troy Ahner
Date: 11/25/2025
Sources:

This is a queue, and a child(priority queue). Used with the intention to be implemented in the design of the find top 10 movies querey


"""
from linkedlist import linkedlist
#need heap implementation in the methodlibrary to create priority queue for O(logn) insertion and pops
from heap import maxheap

class queue: 
    def __init__(self):
        self.__ll = linkedlist()
        #no need to define self.__n because we can just do len(self.__ll)
    
    def enqueue(self,entry):
        self.__ll.push_tail(entry)

    def dequeue(self):
        return self.__ll.pop_head()
    
    def __len__(self):
        return len(self.__ll)
    
    def isempty(self):
        return self.__ll.isempty()

class priorityqueue(queue):
    def __init__(self):
        self.__heap = maxheap() #the queue should be a maxheap

    def enqueue(self,entry):
        self.__heap.push(entry) #push the entry into the maxheap
    
    def dequeue(self):
        #make sure that the heap is not empty
        if self.__heap.isempty():
            raise IndexError("priorityqueue: pop() attempted on empty queue")
        
        return self.__heap.pop() #pop the greatest entry into the maxheap
    
    def __len__(self):
        return len(self.__heap) #the len of the heap has been established so that the number of entries is the length
    
    def isempty(self):
        return self.__heap.isempty() #heap has an isempty() method. If the heap is empty, then the priority queue is empty.
