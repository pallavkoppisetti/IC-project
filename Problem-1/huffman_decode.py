# Creating a function that decodes our huffman encoding, by taking the 
# root of our tree and our encoded text string as parameters

def Decoder(root,encoded_text):
    # Initializing our decoded text string and a temporary pointer that traverses the tree  
    decoded_text=''
    temp=root

    # We pass each bit of our encoded text and accordingly traverse the tree ; 
    # if bit=0 , we move to the left of our current node and right if the bit=1
    # and if we reach a leaf node, we concatenate its symbol to our decoded text 
    # and initialize the temp pointer back to the root node

    for Bits in encoded_text:
        if Bits=='0' and temp.left!=None:
            temp=temp.left
        elif temp.right!=None:
            temp=temp.right

        if temp.left==None and temp.right==None:
            decoded_text+=temp.symbols
            temp=root

# Finally the function outputs the decoded text as a string
    return decoded_text  
