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
        self.__buckets = [linkedlist() for _ in range(NUM_OF_BUCKETS)] #create an array of linkedlists
        self.__m = NUM_OF_BUCKETS #number of buckets. (used to calculate density of hash table)
        self.__n = 0 #number of entries. (used to calculate density of hash table)
    
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

        return result%self.__m
    
    def __resize(self):
        oldsize = self.__m #document the old size
        self.__m *= 2 #double the size of the hash
        newbuckets = [linkedlist() for _ in range(self.__m)] #create a new array of linked lists
        for i in range(oldsize):#iterate through each bucket
            while not self.__buckets[i].isempty():# as long as the current linked list is not empty 
                curr = self.__buckets[i].pop_head() #pop the head of the current linked list
                newbuckets[self._hashfunction(curr)].push_head(curr) #take the current value, and push it into a linked list located at its new
                #bucket
        self.__buckets = newbuckets #reassign the hashtable to this new array of buckets




    #used to add a value to a hash table, if child class has overrode _hashfunction correctly, will still work
    def add(self, value):

        #calculate hash density, if density is greater than 0.75, then resize the hashmap
        if self.__n / self.__m > 0.75:
            self.__resize()

        self.__buckets[self._hashfunction(value)].push_head(value) #hash the value, then push it to the head of the linked list located at that bucket
        #increase number of entries
        self.__n += 1
        return
    
    def contains(self,value):
        #see if the value exists
        return self.__buckets[self._hashfunction(value)].contains(value)



