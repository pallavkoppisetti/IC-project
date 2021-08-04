def Decoder(root,encoded_text):
    decoded_text=''
    temp=root

    for Bits in encoded_text:
        if Bits=='0' and temp.left!=None:
            temp=temp.left
        elif temp.right!=None:
            temp=temp.right

        if temp.left==None and temp.right==None:
            decoded_text+=temp.symbols
            temp=root

    return decoded_text  
