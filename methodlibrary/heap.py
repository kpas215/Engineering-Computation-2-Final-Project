"""
Name: Mason Troy Ahner
Date: 11/27/2025
Sources: Notes from class, a lot of chatGPT to help fix the class example written in collab for the min heap.
(some of the methods made in class were not implemented, while others were just broken or defined incorrectly) 

This is a binary heap. It has two children called maxheap and minheap that overloads the functions for an unspecified binary heap 

"""

class binaryheap:
    def __init__(self):
        self._data = [] #the heap can be implemented by an array
        #keeping this data protected rather than private to be inherited by child implementations of methods
        #none are defined at this moment, but I may eventually want a custom method of one of the children.

    def __len__(self): #overriding __len__ so we can call it in heap implementations
        return len(self._data)
    
    def isempty(self):
        return len(self) == 0 #if the length of the heap is zero, then we know its empty
    
    def peek(self): #peaks the parent root of the heap which is located at index 0
        if self.isempty():
            raise IndexError("binaryheap: peek() called on empty heap")
        return self._data[0]
    
    def push(self, value):
        self._data.append(value) #add the value to the heap
        self._move_up(len(self._data) - 1) #move the data up the heap until it is placed properly

    def pop(self):
        #check to see if popping from an empty heap
        if self.isempty():
            raise IndexError("binaryheap: pop() called on empty heap")
        
        result = self._data[0] #this will be the result of the pop
        new_root = self._data.pop() #remove the last element and decrement the size of the array

        #check to see if the array is empty
        if len(self._data) == 0:
            return result
        
        #if the array is not empty, then overwrite the root with the new root, and then restore the heap
        #by indexing it down until it fits in a proper location

        self._data[0] = new_root #overwriting the old root with the new one
        self._move_down(0) #move the root down to the correct location in the heap

        return result #return the old root.


    #this _better protected method is overidden by max and min heaps, it is used in place of > and < logic used in our heap
    #implementation. By changing how this one method is implemented the rest of our code will work
    #and can function as a minheap or a maxheap on implementation
    def _better(self,a,b) -> bool:
        raise NotImplementedError("binaryheap: _better(a,b) not implemented by child")
    
    def _find_parent_idx(self, i):
        if i == 0:
            return None
        return (i -1)//2

    def _move_up(self, i):
        if not isinstance(i, int):
            raise TypeError("binaryheap: _move_up(i), i must be an int")
        
        while i > 0: #replacing recursive implementation used in class with while loop
            parent_index = self._find_parent_idx(i)

            if parent_index is None:
                break #if the parent_index is none then we know the heap is sorted

            #if the parent_index is not none then we should look at the current parent and child, and see 
            #if we should swap their locations

            if not self._better(self._data[i], self._data[parent_index]):
                break #if the the parent is better than the child, then we dont need to swap, we can end here.

            #if they do need to be swapped, then swap and continue iterating the while loop

            #Originally used additive swap method, but using chatGPT i found out how to swap any datatype in python
            self._data[i], self._data[parent_index] = self._data[parent_index], self._data[i]
            i = parent_index

    def _move_down(self, i):
        #assert that i is an int
        if not isinstance(i, int):
            raise TypeError("binaryheap: _move_down(i), i must be an int")
        
        n = len(self._data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            best = i

            if left < n and self._better(self._data[left], self._data[best]):
                best = left
            if right < n and self._better(self._data[right], self._data[best]):
                best = right

            if best == i:
                break

            #Originally used additive swap method, but using chatGPT i found out how to swap any datatype in python
            self._data[i], self._data[best] = self._data[best], self._data[i]     
            
            i = best

class minheap(binaryheap): #child class that overrides _better(a,b) in the case where parent < child is prefered for sorting data
    def __init__(self):
        super().__init__()

    def _better(self, a, b) -> bool:
        return a < b
    
class maxheap(binaryheap): #child class that overrides _better(a,b) in the case where parent > child is prefered for sorting data
    def __init__(self):
        super().__init__()

    def _better(self, a, b) -> bool:
        return a > b

    