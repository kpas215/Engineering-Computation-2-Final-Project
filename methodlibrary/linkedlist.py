"""
Name: Mason Troy Ahner
Date: 11/23/2025
Sources: my divine intellect

This file is used to create linked lists. designed to be inherited in other data structures such as.
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








