class heapnode:
    def __init__(self,frequency,symbols,left=None,right=None):
        self.frequency=frequency
        self.symbols=symbols
        self.left=left
        self.right=right
        self.bits=''

def huffmantree(leafnodes):
    while len(leafnodes) > 1:
        leafnodes.sort(key=lambda x:x.frequency)

        left=leafnodes[0]
        right=leafnodes[1]

        left.bits=0
        right.bits=1
        
        newHeapNode=heapnode(left.frequency+right.frequency,None,left,right)

        leafnodes.remove(left)
        leafnodes.remove(right)
        leafnodes.append(newHeapNode)

    return leafnodes[0]


def EncodeTable(encode,Treenode,bitstring=''):
    
    codeword=bitstring+str(Treenode.bits)

    if(Treenode.left!=None):
        EncodeTable(encode,Treenode.left,codeword)

    if(Treenode.right!=None):
        EncodeTable(encode,Treenode.right,codeword)

    else:
        encode[Treenode.symbols]=codeword

    return encode