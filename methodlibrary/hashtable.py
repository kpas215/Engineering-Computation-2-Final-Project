"""
Name: Mason Troy Ahner
Date: 11/24/2025
Sources:

This is a dynamically resizing hashmap, using a hash function and a doubly linked list used to handle collisions. 
Ideally this should present an O(1) lookup time, given there are no collisions.


"""

from linkedlist import linkedlist #used to handle collisions. In the case two entries map to the same bucket
NUM_OF_BUCKETS = 20

class hashtable:
    def __init__(self):
        self._buckets = [linkedlist() for _ in range(NUM_OF_BUCKETS)] #create an array of linkedlists
        self._m = NUM_OF_BUCKETS #number of buckets. (used to calculate density of hash table)
        self._n = 0 #number of entries. (used to calculate density of hash table)
    
    #used to hash a value and give a (hopefully) unique and deterministic map to the hash table. Used as a private function
    def _hashfunction(self, value): #i reccommend creating child classes to override this if you plan to insert specific objects
        
        #define the value as a string
        x = str(value)
        #masons hash function from lab_07
        #this one im gonna do a weighted hash, then, multiply by a prime number while simultaneously XORing and bitshifting
        #make x a string
        result = int(0)
        i = int(1307)
        for char in x:
            i +=1
            result ^= 7013* i*ord(char) + (result<<4) #get the weighted sum of ascii characters in the string
            result &= 0xFFFFFFFF

        return result%self._m
    
    def _resize(self): #protected method so we can call it for child hashtable classes
        oldsize = self._m #document the old size
        self._m *= 2 #double the size of the hash
        newbuckets = [linkedlist() for _ in range(self._m)] #create a new array of linked lists
        for i in range(oldsize):#iterate through each bucket
            while not self._buckets[i].isempty():# as long as the current linked list is not empty 
                curr = self._buckets[i].pop_head() #pop the head of the current linked list
                newbuckets[self._hashfunction(curr)].push_head(curr) #take the current value, and push it into a linked list located at its new
                #bucket
        self._buckets = newbuckets #reassign the hashtable to this new array of buckets




    #used to add a value to a hash table, if child class has overrode _hashfunction correctly, will still work
    def add(self, value):

        #calculate hash density, if density is greater than 0.75, then resize the hashmap
        if self._n / self._m > 0.75:
            self._resize()

        self._buckets[self._hashfunction(value)].push_head(value) #hash the value, then push it to the head of the linked list located at that bucket
        #increase number of entries
        self._n += 1
        return
    
    def contains(self,value):
        #see if the value exists
        return self._buckets[self._hashfunction(value)].contains(value)
    
class indexhash(hashtable): #an index based hashtable. You hash by a value, and store its array index in the table,
    #you can get the index back using a get(value) function for O(n) lookup time

    def __init__(self):
        super().__init__()

    def _resize(self): #protected method so we can call and redefine it for child hashtable classes

        #since we now need to store the value AND index in a hash table, we should continue hashing by value but store the 
        #value, index pair in the hash table
        oldsize = self._m #document the old size
        self._m *= 2 #double the size of the hash
        newbuckets = [linkedlist() for _ in range(self._m)] #create a new array of linked lists
        for i in range(oldsize):#iterate through each bucket
            #iterate through each linked list
            for current_entry in self._buckets[i]:
                if current_entry is not None:
                    value, index = current_entry #separate the pair
                    newbuckets[self._hashfunction(value)].push_head((value,index)) #hash by value, insert the pair in the new LL


        self._buckets = newbuckets #reassign the hashtable to this new array of buckets

    def add(self,value,index): #overriding so we can insert value,index pairs
        #calculate hash density, if density is greater than 0.75, then resize the hashmap
        if self._n / self._m > 0.75:
            self._resize()

        self._buckets[self._hashfunction(value)].push_head((value,index)) #hash the value, then push it to the head of the linked list located at that bucket
        #increase number of entries
        self._n += 1
        return
    
    def get(self,value): #new method for indexhash. hashes by value and then gets the index, then we manually traverse the linked list
        #until we find a node that contains a pair of the value we are looking for. finally, we get the index for that pair and return it


        bucket = self._hashfunction(value) #hash the value and get the linked lists location

        for pair in self._buckets[bucket]: #iterate through the linked list
            if pair is not None: #if the linked list is not empty
                stored_value, stored_index = pair
                
                if stored_value == value: #if the value we are looking for is in this pair,
                    #return its index
                    return stored_index

        #if we indexed through the entire list, then return None
        return None 
    
    def contains(self, value):
        if self.get(value) is None:
            return False
        return True











