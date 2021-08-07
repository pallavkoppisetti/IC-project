#import our classes and required functions from the mentioned libraries
from huffman_encode import huffmantree,EncodeTable,heapnode
from collections import defaultdict
from huffman_decode import Decoder

filename='File_1.txt'
# Defining a dictionary for storing the frequency values ,that initializes values to their null value if the key doesnt exist
freq = defaultdict(int)

# running through our text file and incrementing the value associated with a key if we encounter that character
with open(filename) as f:
    for line in f:
        for char in line:
            freq[char] += 1

# Initializing a list that would act as our priority queue and would be storing our heapnodes
leafnodes=[]

# Creating our list that stores the a struct "heapnode"-->that stoes the information about our leaf nodes
for keys,values in freq.items():
    leafnodes.append(heapnode(values,keys))

# The function returns the root node of the huffman tree 
root=huffmantree(leafnodes)

# Dictionary that stores the codewords for each corresponding symbol
encodeTable={}
EncodeTable(encodeTable,root)

# printing out the symbols in our text file and its corresponding codeword
for keys,values in encodeTable.items():
    print(f"{repr(keys)}-->{values}")

size=0
original_size=0

for keys in encodeTable:
    size+=freq[keys]*len(encodeTable[keys])
    original_size+=freq[keys]

# For comparing the file sizes after encoding and before encoding
print(f"\nThe size of our encoded file-->{size}")
print(f"\nThe size of our text file-->{original_size*8}")


# Outputting our encoded file as Encoded_file.txt
with open(filename, 'r') as f, open('Encoded_file.txt', 'w') as outfile:
    for line in f:
        for char in line:
            outfile.write(encodeTable[char])


## Decoding of our encoded text file 
decoded_message=''
encoded_message=''

# Running through our encoded text file and replacing the corresponding codeword with its symbol
# and outputting it as Decoded_file.txt
with open('Encoded_file.txt', 'r') as f, open('Decoded_file.txt', 'w') as outfile:
    for line in f:
        for char in line:
            encoded_message+=char    
    decoded_message=Decoder(root,encoded_message)
    outfile.write(decoded_message)
    
# Code snippet to check for decoding errors
message=''

# Initializing an empty string and storing our text in it
with open(filename) as f:
    for line in f:
        for char in line:
            message+=char

# Comparing the decoded string with our original message string to check for decoding errors
if message==decoded_message:
    print('\nEncoding and decoding of the source file was successful.')
else:
    print('\nError in the decoding!')




     



 