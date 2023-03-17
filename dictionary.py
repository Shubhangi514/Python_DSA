myDict = dict()
print(myDict)
secDict = {}
print(secDict)
engTOsp = {"one": "uno","two":"dos","three":"tres"}
print(engTOsp['three'])
print((hash("three")%len(engTOsp)))

# updating an element in a dictionary

mydict = {'name':'Shubhi','age': 20}
mydict['age'] = 21
mydict['address'] = 'India' # adding a new key 
mydict['education'] = 'B.tech'
print(mydict)

# Traversing through a dictonary  

def traversedict(dict):
    for key in dict:
        print(key , dict[key])
traversedict(mydict) # here time and space complexity is O(n) and O(1)

# Search for an element in a Dictionary

def searchdict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key,value
    return 'the value you are searching for does not exist'
print(searchdict(mydict, 21)) # here time complexity is O(n) and space complexity is O(1)

# Deletion or Removal from Dictionary
 
# print(mydict.pop('name'))
# print(mydict.popitem())
# print(myDict.clear())
# del mydict['age']
# print(mydict)
# print(myDict) # time complexity is O(1) but it is O(n) in amortized case and space complexity is O(1)

# dictionary Methods
 
dict = mydict.copy()
newDict = {}.fromkeys([1,2,3,4,5,6,7,8,9], 0)
print(mydict.setdefault('name1','added'))
print(mydict)
print(mydict.get('number'))
print(mydict.items())
print(mydict.keys())
print(mydict.values())
print(newDict)