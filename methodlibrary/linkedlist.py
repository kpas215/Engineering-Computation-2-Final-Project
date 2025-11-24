"""
Name: Mason Troy Ahner
Date: 11/23/2025
Sources: chatGPT, used to assist in using proper syntax while coding. methods were explicitly made
by me, chatGPT assisted with teaching me how to #include, raise errors, and more.

This file is used to create a doubly linked list. designed to be inherited in other data structures such as.
hashtables

Some slight modification or polymorphism may be required.


"""
from node import doublenode #using the node file

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
        newnode = doublenode(value)

        #if the head doesnt exist, then set the node as the head and the tail
        if self.__head is None:
            self.__head = newnode
            self.__tail = newnode
            self.__n += 1 #increment count of entries
            return 
        
        #if the head did exist, then we know that the tail has been set as well
        #this is because we make sure that we manage the head and tail effectively in all of our methods

        #set the head to point to the new node
        self.__head.set_previous(newnode)

        #set the new node to point to the head
        newnode.set_next(self.__head)
        #set the new node as the new head
        self.__head = newnode
        #increment the count of entries
        self.__n += 1
        return
    
    def push_tail(self,value):
        #create a node containing the current value
        newnode = doublenode(value)

        #if the tail doesnt exist, then set the node as the head and the tail
        if self.__tail is None:
            self.__head = newnode
            self.__tail = newnode
            self.__n += 1 #increment count of entries
            return
        
        #if the tail does exist, then take the node at the tail and have it point to the new node
        self.__tail.set_next(newnode)

        #also make sure to point the new node to the tail
        newnode.set_previous(self.__tail)

        #set the new node as the new tail
        self.__tail = newnode

        #increment the count of entries
        self.__n += 1

    def pop_head(self):
        if self.__head is None:
            raise IndexError("linkedlist: attempted pop_head() on an empty linked list")
        
        result = self.__head.get_data()

        #if there is only one entry (ie the tail is the head), then reset the list
        if self.__tail is self.__head:
            self.__tail = None
            self.__head = None
            self.__n = 0
            return result
        
        #if there is not only one entry, then we can do a normal pop
        newhead = self.__head.get_next() #the new head should be the next node in the list
        
        #assert that newhead is a doublenode
        if not isinstance(newhead, doublenode):
            raise TypeError("linkedlist: attempted pop_head() and the next entry was not a doublenode (impossible?).")
        
        newhead.set_previous(None) #a head should not point to a node head

        self.__head = newhead  #point the head to a new head

        self.__n -= 1 #decrement the count of entries

        return result
    
    def pop_tail(self):
        if self.__tail is None:
            raise IndexError("linkedlist: attempted pop_tail() on an empty linked list")
        
        result = self.__tail.get_data() #get the data from the tail

        #if there is only one entry (ie the tail is the head), then reset the list
        if self.__tail is self.__head:
            self.__tail = None
            self.__head = None
            self.__n = 0
            return result
        
        #if there is not only one entry we can do a normal pop_tail(), 
        newtail = self.__tail.get_previous() #set the new tail to the entry before the tail

        #assert that newtail is a doublenode
        if not isinstance(newtail, doublenode):
            raise TypeError("linkedlist: attempted pop_tail() and the entry before the tail was not a doublenode (impossible?).")
        
        newtail.set_next(None) #the new tail should not point to anything

        self.__tail.set_previous(None) #make the old tail point to nothing.

        self.__tail = newtail #set the tail to the new tail

        #decrement count of entries
        self.__n -= 1

        #return the result

        return result
    
    def get_count(self):
        return self.__n
    
    #peeks the head of the doubly linked list. returns the value stored in the node at the head (if empty, raises an error)
    def peek_head(self):
        if self.__head is None:
            raise IndexError("linkedlist: attempted peek_head() with empty linked list")
        
        return self.__head.get_data()
    
    def peek_tail(self):
        if self.__tail is None:
            raise IndexError("linkedlist: attempted peek_tail() with empty linked list")
        return self.__tail.get_data()
    
    #searches the linked list to see if it contains a certain value. returns a boolean
    def contains(self, value):
        raise NotImplementedError("linkedlist: attempted contains(value), method not currently implemented")
    
    #returns a boolean (True) if the linked list has no entries
    def isempty(self):
        return (self.__n == 1)


        






