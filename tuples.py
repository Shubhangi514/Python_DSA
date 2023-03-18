newTuple = ('a','b','c','d','e')
newTuple1 = tuple('a b c d e')
print(newTuple)
print(newTuple1)
# TC - O(1) SC - O(n) Tuples are unmutable

# Tuples in Memory

print(newTuple[-3]) 
# to access a tuple we also have slice operators
print(newTuple[:2]) 
# traversing a tuple (most commonway to traverse a tuple is through a for loop)

for i in newTuple1:
    print(i)
for i in range(len(newTuple)):
    print(newTuple[i])

# searching an element in a tuple

# first way of searching a tuple is using (in) operator
print('d' in newTuple1)
# second way of searching element is through linear search
def searchTuple(Tuple,element):
    for i in Tuple:
        if i == element:
            return Tuple.index(i)
    return 'the element doest not exist'
print(searchTuple(newTuple,'d'))
# TC-O(n) & SC- O(1)

# Tuple Operation/Functions

print(newTuple + newTuple1)
print(newTuple * 3 )
print(newTuple.count('c') )
print(newTuple.index('e') )
print(len(newTuple1))
print(max(newTuple1))
print(min(newTuple1))
print(tuple([1,2,3,4,5,6]))