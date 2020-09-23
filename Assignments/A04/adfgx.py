"""
  Sarah Gilliland
  CMPS 4663 - Cryptography
  A04 - ADFGX Cipher

  This program reads in keywords from .replit and does one of 2 things depending on the operation "encrypt" or "decrypt".
  If the operation is to "encrypt", the program encrypts a message from the plaintext file and displays the encrypted message in the cyphertext file.
  If the operation is to "decrypt", the program decrypts an encrypted message from the cyphertext file and displays it in the plaintext file.
  The program uses the ADFGX Cipher to encrypt and decrypt the messages.
"""

import sys
import math
import os
from createPolybius import AdfgxLookup

def mykwargs(argv):
    '''
    Processes argv list into plain args (list) and kwargs (dict).
    Just easier than using a library like argparse for small things.
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs


def print_matrix(matrix,rows):
    """ 
    Print the matrix so we can visually confirm that our
    columnar transposition is actually working
    """
    for k in matrix:
        print(k,end=' ')
    print("")
    for k in matrix:
        print('-',end=' ')

    print("")
    for r in range(rows):
        for k in matrix:
            if r < len(matrix[k]):
                print(matrix[k][r],end=" ")
            else:
                print(" ",end=' ')
        print("")


def encrypt(**kwargs):
    """
    Read from the plainText file and call get_message and encrypt_message to encrypt the plain text by the ADFGX Cipher
    """
    with open(infile) as f:
      text = f.read()
    
    text = text.lower()
    print("Plain text: " + text)
    text = text.replace(' ','')

    codedMessage = get_message(text, key1)
    
    encrypt_message(codedMessage)

    

def get_message(text, key1):
    """
    Use the createPolybius file to make a Polybius square and get the new message using key1
    """
    # init and input my first keyword
    A = AdfgxLookup(key1)

    # build my lookup table 
    lookup = A.build_polybius_lookup()

    # print out the actual matrix to the screen
    A.sanity_check()

    message = ''
    # create the message using the lookup table
    for c in text:
      message = (message + ' ' + lookup[c] + ' ')
    print("")

    # get rid of spaces
    message = message.replace(' ','')
    print(message)

    return message



def encrypt_message(message):
    """
    Receive the message from get_message and fill into a matrix with the indices of the letters of key2. 
    Then alphabetize key2 to transpose the columns and mix up the matrix. 
    The encrypted message is the characters of the matrix displayed one by one.
    """
    key2_length = len(key2)             # length of key
    message_length = len(message)       # message length 
    rows = math.ceil(float(message_length)/float(key2_length))

    # dictionary for the new matrix
    matrix = {}

    # every letter is a key that points to a list
    for k in key2:
          matrix[k] = []

    # add the message to the each list in a row-wise fashion
    i = 0
    for m in message:
        matrix[key2[i]].append(m)
        i += 1
        i = i % len(key2)

    print("")
    print_matrix(matrix,rows)

    # Alphabetize the matrix
    temp_matrix = sorted(matrix.items())
    print("")

    sorted_matrix = {}
    # Rebuild the sorted matrix into a dictionary again
    for item in temp_matrix:
        sorted_matrix[item[0]] = item[1]

    # Check what we have
    print_matrix(sorted_matrix,rows)
    print("")

    # Print the cypherText
    print_message(sorted_matrix,key2)



def print_message(matrix,key2word):
    """
    Open the output file and print the message both to the screen and the output file
    """
    ofile = open(outfile, "w")
    
    i = 1
    #print to the screen and to the file
    for k in sorted(key2word):
      for d in matrix[k]:
        print(d,end='') 
        ofile.write(d)
        # the spaces between every two letters is only for appearance
        if i % 2 == 0:
            print(' ',end='')
            ofile.write(' ')
        i += 1
    print("")



def decrypt(**kwargs):
    """
    We have both keys and the cypherText.
    Get the number of long columns so that the matrix can be filled correctly. 
    Fill message into the alphabetized matrix, then unalphabetize.
    Read your message from the amtrix, and then plug it in to the reversed polybius lookup table with the first key and acquire your decrypted plaintext.
    """
    with open(outfile) as f:
      cText = f.read()
    
    cText = cText.replace(' ','')

    ifile = open(infile, "w")
    print("")
    print("Cyphered Text is " + cText)
    print("")
    

    key2_length = len(key2)             # length of key
    cText_length = len(cText)           # message length 
    rows = math.ceil(float(cText_length)/float(key2_length))

    # create empty matrix
    matrix = {k: [] for k in sorted(list(key2))}

    long_cols = cText_length % key2_length
    # integer division, //, gives the number of chars in a column
    col_length = cText_length // key2_length

    long_cols_lookup = []
    short_cols_lookup = []

    for index, column in enumerate(key2):          
      if index < long_cols:
        long_cols_lookup.append(key2[index])
      else:
        short_cols_lookup.append(key2[index])
    
    tempKey2 = sorted(key2)
   
    long_cols_length = col_length + 1
    
    i = 0
    for index, column in enumerate(tempKey2): 
      if tempKey2[index] in long_cols_lookup:
        for _ in range(long_cols_length):
          matrix[column].append(cText[i])
          i += 1
      if tempKey2[index] in short_cols_lookup:
        for _ in range(col_length):
          matrix[column].append(cText[i])
          i += 1

    print_matrix(matrix, rows)
    print("")

    # Alphabetize the matrix
    temp_matrix = { k: matrix[k] for k in key2 }

    print_matrix(temp_matrix,rows)
    print("")

    message = ''
    for r in range(rows):
        for k in temp_matrix:
            if r < len(temp_matrix[k]):
                message = message + temp_matrix[k][r]

    print("Message is " + message)
    
    # Now that you have the message, get the plain text by using each 2 characters as coordinates

    pText = get_plaintext(message, key1)
    print("Plain text is " + pText)
    ifile.write(pText)



def get_plaintext(text, key1):
    """
    Reverse the polybius lookup table and use every 2 letters of the message to find the corresponding plain text character. 
    Concatenate these to get the decrypted plain text.
    """
    B = AdfgxLookup(key1)

    # build my lookup table and reverse it
    lookup2 = B.build_polybius_lookup()
    reverse_lookup = {value : key for (key, value) in lookup2.items()}
    
    B.sanity_check()

    pText = ''
    twoLetters = ""
    i = 1
    # use every 2 letters of the message in the lookup table
    for c in text:
      twoLetters = twoLetters + c
      mod = i % 2
      # if we have read two more letters from the message
      if mod == 0:
        newLetter = reverse_lookup[twoLetters]
        pText = (pText + newLetter)
        twoLetters = ""
      i = i + 1
    
    print("")
    print(pText)
    # return the plain text
    return pText
    


def usage(message=None):
    """
    Display descriptive error messages if the keywords from .replit are incorrect
    """
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [input=string filename] [output=string filename] [key=string] [op=encrypt/decrypt]")
    print(f"Example:\n\t python {name} input=in1 output=out1 op=encrypt key1=machine key2=trex \n")
    sys.exit()

################################################################

if __name__=='__main__':

    required_params = 5 # adjust accordingly

    # get processed command line arguments 
    _,params = mykwargs(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
        usage()

    operation = params.get('op',None)
    infile = params.get('input',None)
    outfile = params.get('output',None)
    key1 = params.get('key1',None)
    key2 = params.get('key2',None)

    if not operation and not infile and not outfile and not key1 and not key2:
        usage()

    if operation == 'encrypt':
        encrypt(**params)
    elif operation == 'decrypt':
        decrypt(**params)
    else:
        usage()
