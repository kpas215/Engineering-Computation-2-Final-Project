'''
Name: Mason Troy Ahner
Date: 11/23/2025
Sources: Lab 04 (from Comp II at temple university)

This file is used to create and modify nodes. designed to be inherited in other data structures such as.
linkedlists
hashtables
trees
graphs

Some slight modification or polymorphism may be required.


'''


class node:
        def __init__(self,data=None,next=None):  #used to create nodes
            self.__data = data #the data of the current node
            self.__next = next #the pointer to the next node

        def set_next(self,next: "node | None"):
              self.__next = next #set the current node to point to the "next" node (specified by the user)

        def set_data(self, data):
              self.__data = data #set the data of the current node to this new data value

        def get_next(self):
              return self.__next
        
        def get_data(self):
              return self.__data
              
class doublenode(node):
        def __init__(self, data=None, next=None, previous=None):
            super().__init__(data, next)
            self.__previous = previous #adding a previous node
        
        def set_previous(self, previous: "doublenode | None"):
              self.__previous = previous

        def get_previous(self):
              return self.__previous
    