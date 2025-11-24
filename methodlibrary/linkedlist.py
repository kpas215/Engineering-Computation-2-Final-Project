"""
Name: Mason Troy Ahner
Date: 11/23/2025
Sources: my divine intellect

This file is used to create linked lists. designed to be inherited in other data structures such as.
hashtables

Some slight modification or polymorphism may be required.


"""

from node import node #using the node file

class linkedlist:
    def __init__(self, firstvalue = None):
        self.__head = None #when initilized we have no head or tail
        self.__tail = None
        self.__n = 0 #used to keep track of how many entries

        #if the firstvalue was specified on init, then push to front
        if firstvalue is not None:
            self.push_head(firstvalue)
    

    def push_head(self, value):
        #create a node containing the current value
        newnode = node(value)

        #if the head doesnt exist, then set the node as the head and the tail
        if self.__head == None:
            self.__head = newnode
            self.__tail = newnode
            self.__n += 1 #increment count of entries
            return 
        
        #if the head did exist, then we know that the tail has been set as well
        #this is because we make sure that we manage the head and tail effectively in all of our methods

        #set the new node to point to the head
        newnode.set_next(self.__head)
        #set the new node as the new head
        self.__head = newnode
        #increment the count of entries
        self.__n += 1
        return

    def push_tail(self, value):
        #create a node containing the current value
        newnode = node(value)

        #if the head doesnt exist, then set the node as the head and the tail
        if self.__head == None:
            self.__head = newnode
            self.__tail = newnode
            self.__n += 1 #increment count of entries
            return 
        
        #if the head did exist, then we know that the tail has been set as well
        #this is because we make sure that we manage the head and tail effectively in all of our methods

        #set the tail node to point to the new node
        self.__tail.set_next(newnode) # type: ignore

        #set the new node as the new tail
        self.__tail = newnode
        #increment the count of entries
        self.__n += 1
        return
    
    def pop_head(self):
        #if the list is empty, throw an error
        if self.__n < 1:
            self.__n = 0 #in the case we somehow broke this, attempt to fix the linked list by wiping everything
            self.__head = None
            self.__tail = None
            raise IndexError("Linked List: Attemped pop_head() on empty list")
        
        #get the value to return
        result = self.__head.get_data() # type: ignore

        #if that was the last entry in the list, then clear the list and return the result
        if self.__n == 1:
            self.__head = None
            self.__tail = None
            self.__n = 0
            return result
        
        #if that was not the last entry in the list, then finally, we just do a normal pop from the head
        #set the head to the node After the head
        self.__head = self.__head.get_next() # type: ignore

        #decrement the count of entries
        self.__n -= 1

        #return the value of the oldhead
        return result

    def pop_tail(self):
        #if the list is empty, throw an error
        if self.__n < 1:
            self.__n = 0 #in the case we somehow broke this, attempt to fix the linked list by wiping everything
            self.__head = None
            self.__tail = None
            raise IndexError("Linked List: Attempted pop_tail() on empty list")
        
        #get the value to return
        result = self.__tail.get_data() # type: ignore

        #if that was the last entry in the list, then clear the list and return the result
        if self.__n == 1:
            self.__head = None
            self.__tail = None
            self.__n = 0
            return result
        
        #if that was not the last entry in the list, then finally, we just do a normal pop from the tail
        #set the head to the node After the head
        self.__head = self.__head.get_next() # type: ignore

        #decrement the count of entries
        self.__n -= 1

        #return the value of the oldhead
        return result







