from huffman_encode import huffmantree,EncodeTable,heapnode
from collections import defaultdict
from huffman_decode import Decoder


freq = defaultdict(int)
with open('File_3.txt') as f:
    for line in f:
        for char in line:
            freq[char] += 1

leafnodes=[]

for keys,values in freq.items():
    leafnodes.append(heapnode(values,keys))

root=huffmantree(leafnodes)

#Codewords for each corresponding symbol
encodeTable={}
EncodeTable(encodeTable,root)

for keys,values in encodeTable.items():
    print(f"{repr(keys)}-->{values}")

size=0
original_size=0

for keys in encodeTable:
    size+=freq[keys]*len(encodeTable[keys])
    original_size+=freq[keys]

print(f"\nThe size of our encoded file-->{size}")
print(f"\nThe size of our text file-->{original_size*8}")


with open('File_3.txt', 'r') as f, open('Encoded_file.txt', 'w') as outfile:
    for line in f:
        for char in line:
            outfile.write(encodeTable[char])

# Decoding 
decoded_message=''
encoded_message=''

with open('Encoded_file.txt', 'r') as f, open('Decoded_file.txt', 'w') as outfile:
    for line in f:
        for char in line:
            encoded_message+=char    
    decoded_message=Decoder(root,encoded_message)
    outfile.write(decoded_message)
    





     



 