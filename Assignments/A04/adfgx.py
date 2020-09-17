"""
  Sarah Gilliland
  CMPS 4663 - Cryptography
  A04 - ADFGX Cipher

  This program reads in keywords from .replit and does one of 2 things depending on the operation "encrypt" or "decrypt". 
  If the operation is to "encrypt", the program encrypts a message from the plaintext file and displays the encrypted message in the cyphertext file. 
  If the operation is to "decrypt", the program decrypts an encrypted message from the cyphertext file and displays it in the plaintext file. 
  The program uses the ADFGX Cipher to encrypt and decrypt the messages.
  
  NOT DONE: so far, the program only encodes. It cannot decrypt yet.
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
    """ Print the matrix so we can visually confirm that our
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
    # should test if file exists ...
    with open(infile) as f:
      text = f.read()
    """
    with open(outfile) as t:
      t.write(codedMessage)
    """
    
    text = text.lower()
    text = text.replace(' ','')
    
    codedMessage = get_message(text, key1)
    

    encrypt_message(codedMessage)

    
    
def get_message(text, key1):
    # init and input my first keyword
    #A = AdfgxLookup('sunflower')
    A = AdfgxLookup(key1)

    # build my lookup table 
    lookup = A.build_polybius_lookup()
    # print out my adfgx lookup table
    # print(lookup)

    # print out the actual matrix
    A.sanity_check()

    message = ''
    #for c in 'dawnarrives':
    for c in text:
      message = (message + ' ' + lookup[c] + ' ')
    print("")

    # get rid of spaces
    message = message.replace(' ','')
    print(message)

    return message



def encrypt_message(message):
    key2_length = len(key2)             # length of key
    message_length = len(message)       # message length 

    # figure out the rows and how many short columns
    rows = math.ceil(float(message_length)/float(key2_length))
    short_cols = key2_length - (message_length%key2_length)

    # dictionary for our new matrix
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

    # Just checking what we have
    print_matrix(sorted_matrix,rows)
    print("")

    # Print the cypherText
    print_message(sorted_matrix,key2)



def print_message(matrix,key2word):
    # Prints the message both to the screen and the output file
    # open the output file
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
    We have both keys and the cypherText, ctext.
    1. Get the number of long columns
    2. Load the letters into your array until you have numLongCols letters left
    3. Then alphabatize your array, and add your remaining letters.
    4. Read your message, and then plug it in to the polybius table with the first key and acquire your decrypted plaintext
    """
    ifile = open(infile, "w")
    print("decrypted message to come...")
    ifile.write("not there yet")

  

def usage(message=None):
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
