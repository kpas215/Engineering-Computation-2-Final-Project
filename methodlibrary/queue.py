"""
Name: Mason Troy Ahner
Date: 11/25/2025
Sources:

This is a queue, and a child(priority queue). Used with the intention to be implemented in the design of the find top 10 movies querey


"""
from linkedlist import linkedlist
#need to a heap implementation in the methodlibrary

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
        raise NotImplementedError("priorityqueue: __init__ not implemented!")

    def enqueue(self,entry):
        raise NotImplementedError("priorityqueue:enqueue(entry) not implemented!")
    
    def dequeue(self):
        raise NotImplementedError("priorityqueue: dequeue() not implemented!")
    
    def __len__(self):
        raise NotImplementedError("priorityqueue: __len__ not implemented!")
    
    def isempty(self):
        raise NotImplementedError("priorityqueue: isempty() not implemented!")
