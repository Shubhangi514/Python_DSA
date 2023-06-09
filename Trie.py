# a trie is a tree base data structure that organizes information in a hierarchy , trie is often used with strings, it is a way for storing words in a way which enables fast lookups
# properties - it is typically used to store strings in a space and time efficient way-any nod in trie can store non repetitive multiple characters-every node stores link of the next character of the string-every node keep track of 'end of string'
# in real world we need trie data structure for modules like spelling checker and auto completion
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
        # since when we create a blank node it will consider it as the end of string so we put false as default 

class Trie:
    def __init__(self):
        self.root = TrieNode()
#  tc = O(1) & sc = O(1)
    # insertion should be done in 4 cases 
    # case1- trie is blank
    # case2- new string prefix is common to another string prefix
    # case3- new string prefix is already present as a complete string 
    # case4- string to be inserted is already presented in trie 
    def inserString(self, word):
        current = self.root 
        for i in word:
            ch = i 
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node  
            # When we commented out the line current = node, it caused the Trie traversal to continue from the root node in each iteration of the loop. As a result, every character of the word was treated as the starting point for a new traversal, and each character was inserted separately as a new branch in the Trie.  
            # For the first character 'A', you correctly created a new TrieNode and updated the current to point to it.
            # For the second character 'P', you did not update current to the newly created TrieNode, so the traversal continued from the root node.
            # As a result, a new branch was created from the root node for the second character 'P' instead of being attached to the previously created node for 'A'.
        current.endOfString = True
        print("Successfully Inserted")
        
    #  tc =  O(m) & sc = O(m) here m is the lenght of the string 

    # trie searching is done in 3 cases:
    # case1- when string is not present at all
    # case2- string is actually present
    # case3- strings prefix is only present not the whole string 
     
    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False

    #  tc =  O(m) & sc = O(1)  

    # trie deletion can be done using 4 cases:
    # case1- some other prefix of the string is same as the one that we want to delete
    # if we want to delete anything in a trie we have to delete it from the leaf node nad not the root 
    # case2- the string is a prefix of another string 
    # case3- other string is a prefix of this string
    # case4- not any node depends on this string

def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if currentNode is None:
        return False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endOfString :
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.inserString("APP")
newTrie.inserString("APPS")
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("APP"))