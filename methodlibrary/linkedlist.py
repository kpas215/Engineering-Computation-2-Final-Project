"""
Name: Mason Troy Ahner
Date: 11/24/2025
Sources: chatGPT, used to assist in using proper syntax while coding, as well as writing tests. methods were explicitly made
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
        curr = self.__head
        while curr is not None:
            if curr.get_data() == value:
                return True
            curr = curr.get_next()
        return False
    
    #returns a boolean (True) if the linked list has no entries
    def isempty(self):
        return (self.__n == 0)


#tests generated by chatGPT
if __name__ == "__main__":
    print("Running linkedlist.py internal tests...")

    # Helper function to assert conditions
    def assert_equal(a, b, message=""):
        if a != b:
            raise AssertionError(f"ASSERTION FAILED: {a} != {b}. {message}")
        else:
            print(f"✓ {message}")

    def assert_raises(exception_type, func, message=""):
        try:
            func()
        except exception_type:
            print(f"✓ {message}")
            return
        except Exception as e:
            raise AssertionError(f"Wrong exception raised: {e}")
        raise AssertionError(f"Expected {exception_type.__name__} but nothing was raised. {message}")

    print("\n=== TEST 1: Empty list behavior ===")
    ll = linkedlist()
    assert_equal(ll.get_count(), 0, "empty list count = 0")
    assert_raises(IndexError, ll.peek_head, "peek_head on empty raises")
    assert_raises(IndexError, ll.peek_tail, "peek_tail on empty raises")
    assert_raises(IndexError, ll.pop_head, "pop_head on empty raises")
    assert_raises(IndexError, ll.pop_tail, "pop_tail on empty raises")

    print("\n=== TEST 2: push_head single ===")
    ll = linkedlist()
    ll.push_head(10)
    assert_equal(ll.get_count(), 1, "count after one push_head")
    assert_equal(ll.peek_head(), 10, "peek_head returns pushed value")
    assert_equal(ll.peek_tail(), 10, "peek_tail returns pushed value")

    print("\n=== TEST 3: push_tail single ===")
    ll = linkedlist()
    ll.push_tail(20)
    assert_equal(ll.get_count(), 1, "count after one push_tail")
    assert_equal(ll.peek_head(), 20, "peek_head matches")
    assert_equal(ll.peek_tail(), 20, "peek_tail matches")

    print("\n=== TEST 4: push_head multiple ===")
    ll = linkedlist()
    ll.push_head(1)
    ll.push_head(2)
    ll.push_head(3)
    assert_equal(ll.get_count(), 3, "count after push_head x3")
    assert_equal(ll.peek_head(), 3, "head is last pushed")
    assert_equal(ll.peek_tail(), 1, "tail is first pushed")
    assert_equal(ll.pop_head(), 3, "pop_head removes 3")
    assert_equal(ll.peek_head(), 2, "new head is 2")
    assert_equal(ll.peek_tail(), 1, "tail unchanged")
    assert_equal(ll.get_count(), 2, "count decremented")

    print("\n=== TEST 5: push_tail multiple ===")
    ll = linkedlist()
    ll.push_tail(1)
    ll.push_tail(2)
    ll.push_tail(3)
    assert_equal(ll.get_count(), 3, "count after push_tail x3")
    assert_equal(ll.peek_head(), 1, "head is first pushed")
    assert_equal(ll.peek_tail(), 3, "tail is last pushed")
    assert_equal(ll.pop_tail(), 3, "pop_tail removes 3")
    assert_equal(ll.peek_tail(), 2, "new tail is 2")
    assert_equal(ll.get_count(), 2, "count decremented")

    print("\n=== TEST 6: mixed pushes/pops ===")
    ll = linkedlist()
    ll.push_head(2)      # [2]
    ll.push_tail(3)      # [2, 3]
    ll.push_head(1)      # [1, 2, 3]
    ll.push_tail(4)      # [1, 2, 3, 4]
    assert_equal(ll.peek_head(), 1, "head = 1")
    assert_equal(ll.peek_tail(), 4, "tail = 4")
    assert_equal(ll.pop_head(), 1, "pop_head")
    assert_equal(ll.pop_tail(), 4, "pop_tail")
    assert_equal(ll.peek_head(), 2, "new head = 2")
    assert_equal(ll.peek_tail(), 3, "new tail = 3")
    assert_equal(ll.get_count(), 2, "count = 2")

    print("\n=== TEST 7: pop until empty (head) ===")
    ll = linkedlist()
    for i in range(5):
        ll.push_tail(i)
    popped = [ll.pop_head() for _ in range(5)]
    assert_equal(popped, [0,1,2,3,4], "pop_head drains list correctly")
    assert_equal(ll.get_count(), 0, "count = 0 after draining")

    print("\n=== TEST 8: pop until empty (tail) ===")
    ll = linkedlist()
    for i in range(5):
        ll.push_tail(i)
    popped = [ll.pop_tail() for _ in range(5)]
    assert_equal(popped, [4,3,2,1,0], "pop_tail drains list backwards")
    assert_equal(ll.get_count(), 0, "count = 0 after draining")

    print("\n=== TEST 9: constructor with firstvalue ===")
    ll = linkedlist(firstvalue=99)
    assert_equal(ll.get_count(), 1, "count = 1")
    assert_equal(ll.peek_head(), 99, "head = 99")
    assert_equal(ll.peek_tail(), 99, "tail = 99")

    print("\n=== TEST 10: contains(value) ===")

    ll = linkedlist()
    ll.push_tail(10)
    ll.push_tail(20)
    ll.push_tail(30)

    # True cases
    assert_equal(ll.contains(10), True, "contains(10) should be True")
    assert_equal(ll.contains(20), True, "contains(20) should be True")
    assert_equal(ll.contains(30), True, "contains(30) should be True")

    # False case
    assert_equal(ll.contains(999), False, "contains(999) should be False")

    # Edge case: contains on empty list
    empty = linkedlist()
    assert_equal(empty.contains(5), False, "contains on empty list should be False")

    print("✓ contains(value) tests passed")

    print("\nALL TESTS PASSED SUCCESSFULLY 🎉\n")


        






