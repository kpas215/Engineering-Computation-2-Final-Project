"""
Name: Mason Troy Ahner
Date: 11/24/2025
Sources: ChatGPT for implementing tests. 

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

    def get_m(self):
        return self._m
    
    def get_n(self):
        return self._n


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
    
    def __len__(self): #used to determine how many entries are in the hashtable
        return self._n
    
    def isempty(self):
        return (self._n == 0)
    
class indexhash(hashtable): #an index based hashtable. You hash by a value, and store its array index in the table,
    #you can get the index back using a get(value) function for an ideal O(1) lookup time

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

#tests generated by chatGPT
if __name__ == "__main__":
    print("Running hashtable.py internal tests...\n")

    tests_passed = 0
    tests_ran = 0

    def check(condition, name):
        global tests_passed, tests_ran
        tests_ran += 1
        if condition:
            print(f"✓ {name}")
            tests_passed += 1
        else:
            print(f"✗ {name}")


    # =========================
    # TEST GROUP 1: hashtable
    # =========================
    print("=== Testing hashtable ===")

    # Test 1: initial state
    h = hashtable()
    check(h.get_m() == NUM_OF_BUCKETS, "hashtable: initial m == NUM_OF_BUCKETS")
    check(h.get_n() == 0, "hashtable: initial n == 0")

    # Test 2: add without resize (stay under load factor threshold)
    h2 = hashtable()
    # load factor threshold: > 0.75 triggers resize
    # 0.75 * 20 = 15, so up to 15 inserts should NOT resize
    for i in range(15):
        h2.add(i)
    check(h2.get_m() == 20, "hashtable: no resize when n/m == 0.75")
    check(h2.get_n() == 15, "hashtable: n updated correctly without resize")

    # Test 3: add with resize (cross load-factor threshold)
    h3 = hashtable()
    # Insert 17 elements: at n=16, 16/20=0.8 > 0.75, so resize should trigger
    for i in range(17):
        h3.add(i)
    check(h3.get_m() == 40, "hashtable: resize triggers when n/m > 0.75")
    check(h3.get_n() == 17, "hashtable: n correct after resize")

    # Test 4: contains() basic behavior
    h4 = hashtable()
    for i in range(10):
        h4.add(i)
    check(h4.contains(0), "hashtable: contains() returns True for inserted value (0)")
    check(h4.contains(9), "hashtable: contains() returns True for inserted value (9)")
    check(not h4.contains(999), "hashtable: contains() returns False for missing value")

    # Test 5: contains() after resize
    h5 = hashtable()
    # trigger a resize and test contents preserved
    for i in range(25):     # this will definitely force a resize
        h5.add(i)
    check(h5.get_m() > 20, "hashtable: resized for larger input")
    check(h5.contains(0), "hashtable: contains() still works for 0 after resize")
    check(h5.contains(24), "hashtable: contains() still works for last inserted value")
    check(not h5.contains(999), "hashtable: contains() correctly False after resize")

    # Test 6: duplicates
    h6 = hashtable()
    h6.add("hello")
    h6.add("hello")
    check(h6.contains("hello"), "hashtable: contains() True for duplicate key")
    check(h6.get_n() == 2, "hashtable: n counts duplicates as separate entries")

    # =========================
    # TEST GROUP 2: indexhash
    # =========================
    print("\n=== Testing indexhash ===")

    # Test 7: basic add/get
    ih1 = indexhash()
    ih1.add("star wars", 0)
    ih1.add("star trek", 1)
    ih1.add("matrix", 2)
    check(ih1.get("star wars") == 0, "indexhash: get() returns correct index for 'star wars'")
    check(ih1.get("star trek") == 1, "indexhash: get() returns correct index for 'star trek'")
    check(ih1.get("matrix") == 2, "indexhash: get() returns correct index for 'matrix'")

    # Test 8: get() for missing value
    check(ih1.get("shrek") is None, "indexhash: get() returns None for missing value")

    # Test 9: contains() uses get()
    check(ih1.contains("star wars"), "indexhash: contains() True for present key")
    check(not ih1.contains("lord of the rings"), "indexhash: contains() False for missing key")

    # Test 10: behavior with duplicate keys (last index wins or first is fine)
    # Since you return the first matching index, we just check it's one of the inserted indices.
    ih2 = indexhash()
    ih2.add("dup", 5)
    ih2.add("dup", 10)
    idx = ih2.get("dup")
    check(idx in (5, 10), "indexhash: get() returns one of the indices for duplicate keys")

    # Test 11: resize behavior preserves mappings
    ih3 = indexhash()
    # Force resize (similar logic: > 0.75 load factor)
    # For m=20, > 15 entries triggers resize
    for i in range(18):
        ih3.add(f"key_{i}", i)
    resized_m = ih3.get_m()
    check(resized_m > 20, "indexhash: resize triggered for large number of entries")
    # Check a few mappings after resize
    check(ih3.get("key_0") == 0, "indexhash: get('key_0') correct after resize")
    check(ih3.get("key_5") == 5, "indexhash: get('key_5') correct after resize")
    check(ih3.get("key_17") == 17, "indexhash: get('key_17') correct after resize")
    check(ih3.get("missing_key") is None, "indexhash: get() still None for missing after resize")
    check(ih3.contains("key_10"), "indexhash: contains() True for present key after resize")
    check(not ih3.contains("does_not_exist"), "indexhash: contains() False for missing key after resize")

    # Summary
    print(f"\n{tests_passed}/{tests_ran} tests passed.")
    if tests_passed == tests_ran:
        print("ALL TESTS PASSED 🎉")
    else:
        print("SOME TESTS FAILED ❌")



