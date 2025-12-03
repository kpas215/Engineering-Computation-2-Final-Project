"""
Name: Mason Troy Ahner
Date: 11/25/2025
Sources:

This is a queue, and a child(priority queue). Used with the intention to be implemented in the design of the find top 10 movies querey


"""
from linkedlist import linkedlist

class Queue:  # Changed to capital Q
    def __init__(self):
        self.__ll = linkedlist()
    
    def enqueue(self, entry):
        self.__ll.push_tail(entry)

    def dequeue(self):
        return self.__ll.pop_head()
    
    def __len__(self):
        return len(self.__ll)
    
    def is_empty(self):  # Added underscore version for consistency
        return self.__ll.isempty()
    
    def isempty(self):  # Keep original for compatibility
        return self.__ll.isempty()

class priorityqueue(Queue):
    def __init__(self):
        raise NotImplementedError("priorityqueue: __init__ not implemented!")

    def enqueue(self, entry):
        raise NotImplementedError("priorityqueue:enqueue(entry) not implemented!")
    
    def dequeue(self):
        raise NotImplementedError("priorityqueue: dequeue() not implemented!")
    
    def __len__(self):
        raise NotImplementedError("priorityqueue: __len__ not implemented!")
    
    def isempty(self):
        raise NotImplementedError("priorityqueue: isempty() not implemented!")