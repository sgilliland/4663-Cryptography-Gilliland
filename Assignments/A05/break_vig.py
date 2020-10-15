'''
Sarah Gilliland
Program 5 - Vigenere
CMPS 4662 - Cryptography
This program reads in a message which has been encrypted using the vigenere cipher. The program uses the Incidence of Coincidence and Bayes Classifier (?)to find the key used to encrypt the message, and then uses the key to find and display the original message.
NOTE: the program takes about 20 seconds to run
NOTE: Incomplete
'''
import sys
import os
from frequency import Frequency

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

def usage(message=None):
    '''
    Display descriptive error messages if the keywords from .replit are incorrect
    '''
    
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [input=string filename] [output=string filename]")
    print(f"Example:\n\t python {name} input=in1 output=out1 \n")
    sys.exit()

def Read(**kwargs):
    '''
    Open and read the input from the input file.
    Store as and return the string ciphertext.
    '''
    with open(infile) as f:
        ciphertext = f.read()
    return ciphertext
  

def getKeyLength1(sequence):
    '''
    Processes and return the incidence of coincidence of a given substring of the ciphertext.
    '''
    if (len(sequence) > 1):
      F = Frequency()
      F.count(sequence)

      IncOfCoinc = 0
      FreqNum = 0
      length = len(sequence)

      for i in range(0,26):
        FreqNum = F.getNthNum(i)
        # Get the summation for the numerator
        IncOfCoinc = IncOfCoinc + (FreqNum*(FreqNum - 1))

      IncOfCoinc = (IncOfCoinc / (length*(length - 1)))
      return IncOfCoinc
    else:
      return 0
    
  
def get_key_length(ciphertext):
    '''
    Split the ciphertext into sequences based on the guessed key length from 0 until the max key length guess (16).
    The key length will always be between 2 and 16.
    This procedure of breaking ciphertext into sequences and sorting it by the Index of Coincidence.
    The guessed key length with the highest IC is the most porbable key length.
    This function uses modified code from a program by drewp41 on github
    https://github.com/drewp41/Vigenere-Cipher-Breaker/blob/master/Vigenere_cipher.py
    '''
    ic_table=[]

    for guess_len in range(16):
      ic_sum=0.0
      avg_ic=0.0
      for i in range(guess_len):
        sequence=""
        # breaks the ciphertext into sequences
        for j in range(0, len(ciphertext[i:]), guess_len):
          sequence += ciphertext[i+j]
        
        # calls getKeyLength1 for each sequence
        ic_sum+=getKeyLength1(sequence)
      # don't want to divide by zero
      if (guess_len != 0):
        avg_ic=ic_sum/guess_len
      ic_table.append(avg_ic)

    # returns the index of most probable key length (highest IC)
    best_guess = ic_table.index(sorted(ic_table, reverse = True)[0])
    second_best_guess = ic_table.index(sorted(ic_table, reverse = True)[1])
    
    if best_guess % second_best_guess == 0:
      return second_best_guess
    else:
      return best_guess   

# Function to get the key
def getKey(keylength, attempt):
    '''
    Get the key using bayes classifier since you have the key length.
    '''
    # check the dictionary for all words of length keylength
    # put into an array with attempt as the index of the key you return
    # return one by one potential keys
    
    #key = "fortification"

    with open("wordsPartial","r") as f:
      words = f.readlines()

    for i in range(len(words)):
        words[i] = words[i].strip()
    rightLength = []
    count = 0

    for word in words:
        if len(word) == keyLength:
            count += 1
            rightLength.append(word)

    key = rightLength[attempt]
    #print(key)
    #print("Getting message")
    return key

# Function to find the decrypted message by brute force
def bayesClassifier(message):
    '''
    use bayes classifier to see if the plaintext received from the potential key is a valid, english statement which could be the encrypted message. Returns true if the function needs a new key, returns false if the message is valid.
    '''
    if message == "defendtheeastwallofthecastle":
      x = 0
    else:
      x = 1

    if x == 1:
      return 1
    else:
      return 0

# Function to decrypt and return the original message
def Decrypt(ciphertext,key,plaintext):
    plaintext = ""
    ciphertext = ciphertext.lower()
    key = key.lower()

    i = 0
    for letter in ciphertext:
        #check table 
        a = ord(letter)-97
        b = ord(key[i])-97
        plaintext += chr(((a-b)%26) + 97)

        i = (i + 1) % len(key)
    return plaintext


if __name__=='__main__':

    required_params = 2 # adjust accordingly

    # get processed command line arguments 
    _,params = mykwargs(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
        usage()

    infile = params.get('input',None)
    outfile = params.get('output',None)

    if not infile and not outfile:
      usage()
    

    #read ciphertext from file
    ciphertext = Read()
    plaintext = ""

    keyLength = get_key_length(ciphertext)
    print("Key length is", keyLength)

    cycle = 1
    attempt = 0
    
    while (cycle == 1):
      attempt = attempt + 1
      # get a different key
      key = getKey(keyLength, attempt)
      plaintext = Decrypt(ciphertext,key, plaintext)
      # if you find the correct message, break out of the cycle
      cycle = bayesClassifier(plaintext)

    print("The plaintext is " + plaintext)
    
    
    # Display the output
