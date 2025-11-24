class node:
        def __init__(self,data=None,next=None):  #used to create nodes
            self.__data = data #the data of the current node
            self.__next = next #the pointer to the next node

        def set_next(self,next: "node"):
              self.__next = next #set the current node to point to the "next" node (specified by the user)

        def set_data(self, data):
              self.__data = data #set the data of the current node to this new data value

        def get_next(self):
              return self.__next
        
        def get_data(self):
              return self.__data
              
        