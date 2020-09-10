
## Assignment 3 - Frequency Analysis
#### Name: Sarah Gilliland
#### Due: Tuesday, September 8, 2020

### General Problem
I received two files that were encrypted using a "substitution" cipher. The genius whom encrypted these, randomly shuffled a list of letters multiple times. The problem is, he never sent me the key! So, I cannot reverse the process. I need your help to decipher these messages.

It is not a shift cipher, so you cant brute force the shift value! So the only way to get these two messages vital to the safety of earth is to run a frequency analysis on them. Below is a typical frequency distribution for you to work with.

#### Typical Frequency Distribution Graph
<a href="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/frequency_4663_2020.jpg"><img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/frequency_4663_2020.jpg" width="600"></a>

### First (easy)
Run a frequency analysis on the file in1.txt and substitute each letter based on the calculated frequency using the table below. Punctuation is left for readability. All words are english words and the frequency distribution is a perfect match for the graph at the top.

### Second (medium)
Now do the same for in2.txt and substitute again based on frequency. This one doesn't line up perfectly, but close enough to not make it too hard. This one is not as common as the first. But it is part of an extremely famous book. And part of a famous movie rant.


### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [FirstDecryptionSteps.pdf](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A03/FirstDecryptionSteps.pdf)     | PDF of 1st decryption process  |
|   2   | [SecondDecryptionSteps.pdf](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A03/SecondDecryptionSteps.pdf)     | PDF of 2nd decryption process  |
|   3   | [FrequencyAnalysis.py](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A03/FrequencyAnalysis.py)     | Program to analyze letter frequency   | 
|   4   | [in1.txt](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A03/in1.txt)               | First encryption input                 |
|   5   | [in2.txt](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A03/in2.txt)               | Second encryption input                |


### Sources (example)
- I used and edited code for the frequency analysis from Dr. Griffin.
