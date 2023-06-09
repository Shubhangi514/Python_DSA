# Hashing- is a mthond of sorting and indexing data . The idea behind hashing is to allow large amount of data to be indexed using keys commonly created by formulas
# Why Hasing? it is time efficient in case of search operations
# Hash Function : It is a function that can be used to map of arbitrary size to data of fixed size
# key : input data given by the user
# hash Value: A value that is returned by hash function
# hash Table : it is a data structure which implements an associative array abstract data type a structure that can map key to values
# collision : it ocurs when two different keys to a hash function produces the same output
# properties of good hash function:-
# (1)it distributes hash values uniformly across hash table (2)it has to use all input data 
# types of resolution techniques for collision- (1)Direct Chaining :- Implementing the buckets as linked list . Colliding elements are stored in this lists
# (2)Open Addressing :- colliding elements are stored in other vaant buckets. during storage and lookup these are found through so called probing [(a)Linear Probing :- it places new key into closest following empty cell (b)Quadratic Probing :- adding arbitrary quadratic polynomial to the index until an empty cell is found (c)Double Hashing :- interval between probes is computed by another hash function] 
# what to do when the given hash table is full?  (1) firstly in case of DIRECT CHAINING this will never occur as linked lists will be creating continously (2) but in case of OPEN ADDRESSING when the table is full we need to create a new hash table of double the size and then generate hash values all over again for every inputed value and then we will inplement them linearly this case can be very time consuming and can cause time complexity upto O(n)
# Pros & Cons of Collision resolution techniques :- (1)DirectChaining:(a)hash table never gets full(pro)(b)huge linked list causes performances leaks i.e time complexity of search operation becomes O(n)(con)(2)OpenAddressing:(a)Easy implementation(pro)(b)when hash table is full creation of new hash table affects performance i.e time complexity becomes O(n)(con)
# when to use which resolution technique:-if the input size is kmown we always use "Open Addressing" - if we perform deletion operation frequently we use "Direct Chaining"
# practical use of hashing : 
# (1) passwords on servers- so whenever we enter our password it takes the value convertes it into hash value and stores it into servers so the next time when we enter our password the hash function converts the key value to hash value to access then the server checks if this value if present in the table or not (hashing is used in password authentication)
# (2) file systems- file path is mapped to the physical location on the disk 
def mod(number, cellNumber):
    return number % cellNumber


# print(mod(400, 24))


def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

print(modASCII("ABC", 24))

 