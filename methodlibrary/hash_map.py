'''
Movie Database Project - HashMap Class

Description: HashMap implementation with key-value pairs using chaining for collision handling

@Author: Ian MacCabe
@Contact: ian.maccabe@temple.edu    
@Date: [Your Date]

Sources: 
    Based on lab_04 hash table implementation
'''

#####################################################################
## Basic linked list class
#####################################################################
class linked_list:
    '''standard linked list class'''

    class node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = self.node(data=value, next=self.head)
        self.head = new_node

    def lookup(self, target=None, field=None):
        curr_ptr = self.head
        ret_val = []

        while curr_ptr is not None:
            if hasattr(curr_ptr.data, field) and \
                getattr(curr_ptr.data, field) == target:
                    ret_val.append(curr_ptr.data)
            curr_ptr = curr_ptr.next

        return ret_val
    
    def remove(self, target=None, field=None):
        if self.head is None:
            return False
        
        if hasattr(self.head.data, field) and \
            getattr(self.head.data, field) == target:
            self.head = self.head.next
            return True
        
        curr_ptr = self.head
        while curr_ptr.next is not None:
            if hasattr(curr_ptr.next.data, field) and \
                getattr(curr_ptr.next.data, field) == target:
                curr_ptr.next = curr_ptr.next.next
                return True
            curr_ptr = curr_ptr.next
        
        return False
    
    def get_all(self):
        result = []
        curr_ptr = self.head
        while curr_ptr is not None:
            result.append(curr_ptr.data)
            curr_ptr = curr_ptr.next
        return result


#####################################################################
## HashMap class with key-value pairs
#####################################################################
class HashMap:
    '''HashMap implementation with chaining for collisions'''

    class node:
        def __init__(self, k, v):
            self.key = k
            self.value = v

    def __init__(self, array_len=50):
        self.__buffer = [linked_list() for _ in range(array_len)]
        self.__array_len = array_len
        self.__size = 0

    def _hash_function(self, key):
        '''Hash function for string keys'''
        
        key_str = str(key)
        
        if not key_str:
            return 0
        
        s = ord(key_str[0])
        if len(key_str) > 1:
            s += ord(key_str[1]) * 19

        for ch in key_str[2:]:
            s *= ord(ch)

        return s % self.__array_len

    def put(self, key, value):
        '''Insert or update a key-value pair'''
        
        index = self._hash_function(key)
        
        existing = self.__buffer[index].lookup(target=key, field='key')
        
        if existing:
            existing[0].value = value
        else:
            self.__buffer[index].insert(self.node(key, value))
            self.__size += 1

    def get(self, key):
        '''Retrieve value associated with key'''
        
        index = self._hash_function(key)
        result = self.__buffer[index].lookup(target=key, field='key')
        
        if result:
            return result[0].value
        return None

    def contains(self, key):
        '''Check if key exists in HashMap'''
        
        index = self._hash_function(key)
        result = self.__buffer[index].lookup(target=key, field='key')
        return len(result) > 0

    def remove(self, key):
        '''Remove a key-value pair'''
        
        index = self._hash_function(key)
        removed = self.__buffer[index].remove(target=key, field='key')
        
        if removed:
            self.__size -= 1
        return removed

    def get_all_keys(self):
        '''Return array of all keys in the HashMap'''
        
        keys = []
        for bucket in self.__buffer:
            nodes = bucket.get_all()
            for node in nodes:
                keys.append(node.key)
        return keys

    def get_all_values(self):
        '''Return array of all values in the HashMap'''
        
        values = []
        for bucket in self.__buffer:
            nodes = bucket.get_all()
            for node in nodes:
                values.append(node.value)
        return values

    def size(self):
        '''Return number of key-value pairs'''
        return self.__size

    def is_empty(self):
        '''Check if HashMap is empty'''
        return self.__size == 0