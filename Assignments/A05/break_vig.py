'''
Sarah Gilliland
Program 5 - Vigenere
CMPS 4662 - Cryptography
This program reads in a message which has been encrypted using the vigenere cipher. 
The program uses the Incidence of Coincidence to find the key used to encrypt the message, 
and then uses the key to find the original message. 
'''
import sys
import os
from frequency import Frequency
from math import log

# Build a cost dictionary, assuming Zipf's law
# cost = -math.log(probability)
freqWords = open("words-by-frequency.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(freqWords)))) for i,k in enumerate(freqWords))
maxword = max(len(x) for x in freqWords)


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


def read(**kwargs):
    '''
    Open and read the input from the input file.
    Store as and return the string ciphertext.
    '''
    with open(infile) as f:
        ciphertext = f.read()
    return ciphertext
  

def incidence_of_coincidence(sequence):
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
        
        # calls incidence_of_coincidence function for each sequence
        ic_sum+=incidence_of_coincidence(sequence)
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


def get_key(keylength, attempt,words):
    '''
    Search the dictionary for all words of length keylength.
    Put into an array with attempt as the index of the key you return.
    Return one by one potential keys
    '''
    #key = "fortification" for input1

    for i in range(len(words)):
        words[i] = words[i].strip()
    rightLength = []
    count = 0

    for word in words:
        if len(word) == keyLength:
            count += 1
            rightLength.append(word)

    key = rightLength[attempt]
    return key


def check_english(message, words):
    '''
    Check to see if the plaintext received from the potential key is a valid, english statement which could be the encrypted message. Return the probability ratio of likliness for English.
    '''
    tokens = message.split()
    score = 0
    for tok in tokens:
        if tok.upper() in words:
            score += 1

    return score / len(tokens)


def decrypt(ciphertext, key, plaintext):
    # Decrypt using the key and return the plaintext
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


def infer_spaces(s):
    """
    Uses dynamic programming to infer the location 
    of spaces in a string without spaces.
    https://controlc.com/c1666a6b
    """
    # Find the best match for the i first characters, assuming cost hasbeen built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))


if __name__=='__main__':

    required_params = 2

    # get processed command line arguments 
    _,params = mykwargs(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
        usage()

    infile = params.get('input',None)
    outfile = params.get('output',None)

    if not infile and not outfile:
      usage()
    
    with open("words","r") as f:
      words = f.readlines()
    
    for i in range(len(words)):
        words[i] = words[i].strip();

    #read ciphertext from file
    ciphertext = read()
    #strip ciphertext of its spaces
    plaintext = ""

    keyLength = get_key_length(ciphertext)
    print("Key length is", keyLength)

    cycle = 1
    attempt = 0
    
    while (cycle == 1):
      attempt = attempt + 1
      # get a different key, decrypt, and check if it's english
      key = get_key(keyLength, attempt, words)
      plaintext = decrypt(ciphertext, key, plaintext)
      plaintext = infer_spaces(plaintext)
      ratio = check_english(plaintext,words)

      # if you find the correct message, break out of the cycle
      if (ratio >= 0.8):
        cycle = 0
      
    print("The plaintext is " + plaintext)
