## Assignment 5 - Vigenere Cracking
#### Name: Sarah Gilliland
#### Due: Tuesday, September 29, 2020

### General Problem
Decrypt a file which was encrypted by the Vigenere Algorithm.
Write a python program that will discover the size of that dictionary word (keylength) and then determine which word was used to encrypt your file(s).

### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [break_vig.py](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A05/break_vig.py)     | Main program used for this assignment       |
|   2   | [frequency.py](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A05/frequency.py)     | Frequency class sorts an alphabet by the frequency of letters in a given message    |
|   3   | [words](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A05/words)     | List of 45333 words in the English Dictionary    |
|   4   | [words-by-frequency.txt](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A05/words-by-frequency.txt)     | List of 125549 words in the English Dictionary sorted by frequency    |
|   5   | [input1](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A05/input1)     | Input file to read in the encrypted text       |
|   6   | [output1](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A05/output1)     | Output file to display the keylength, keyword, and plain text       |
|   7   | [input2](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A05/input2)     | Input file used for testing code       |
|   8   | [output2](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A05/output2)     | Output file used for testing code       |


### Sources
- I used the following website to split the message into a sentence with spaces: [clickHere](https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words)
- I used the following program by drewp41 on github for my implementation of incidence of coincidence: [clickHere](https://github.com/drewp41/Vigenere-Cipher-Breaker/blob/master/Vigenere_cipher.py)
- I used the following website to find information on the library langdetect: [clickHere](https://pypi.org/project/langdetect/)
