# Defining a class called heapnode that has stores the symbol,frequency of the symbol, pointer to each of its children
# and a flag variable called "bits" which denotes if its the left child or the right child 
class heapnode:
    def __init__(self,frequency,symbols,left=None,right=None):
        self.frequency=frequency
        self.symbols=symbols
        self.left=left
        self.right=right
        self.bits=''


# Function that creates our huffman tree by taking our priority queue as input and outputs the root node
# We first sort the queue by frequency and define the parent of these leafnode, with frequency as the sum of
# the frequncies of the first two nodes of our sorted priority queue. We then pop off those two nodes
# and push our newnode into our queue and sort it again. We repeat this process till the size of our priority queue is 1.

def huffmantree(leafnodes):
    while len(leafnodes) > 1:
        # sorting our queue
        leafnodes.sort(key=lambda x:x.frequency)

        
        left=leafnodes[0]
        right=leafnodes[1]

        # Defining the flags variables and pointers of our nodes

        left.bits=0
        right.bits=1
        
        # defining our new parent node of our huffman tree
        newHeapNode=heapnode(left.frequency+right.frequency,None,left,right)
        
        # popping the first two elements and pushing our parent node
        leafnodes.remove(left)
        leafnodes.remove(right)
        leafnodes.append(newHeapNode)

    # returning our final root node
    return leafnodes[0]


# A function that creates a dictionary that stores our symbols as our key and its codeword as its keyvalue
def EncodeTable(encode,Treenode,bitstring=''):
    
    # codeword variable stores our code word, where as we move down the tree the corresponding bit gets concatenated
    codeword=bitstring+str(Treenode.bits)

    # if the left node isn't NULL, we recursively call the function to traverse the tree till we can go any further
    # and then check if we can go to the right while going back ( this is basically similar to DFS of a tree)
    if(Treenode.left!=None):
        EncodeTable(encode,Treenode.left,codeword)

    if(Treenode.right!=None):
        EncodeTable(encode,Treenode.right,codeword)

    # if we both left and right children are NULL, that means we have reached the leafnode and we
    # have found its corresponding codeword
    else:
        encode[Treenode.symbols]=codeword

    return encode