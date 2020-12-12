## Assignment 8 - Public Key Encryption
#### Name: Sarah Gilliland
#### Completed: Saturday, December 12, 2020

### General Problem
This project will use an existing python library called [cryptography](https://cryptography.io/en/latest/index.html) (appropriately named) to use public key encryption 
to encrypt and decrypt messages sent between two entities.  We will use a library called Flask to allow two scripts
to "talk" or communicate over a network (NOT on the same computer). 
A Flask server runs and "listens" or monitors a "port" on a computer. When requests are directed to that port either from
an internal request or an external request, they are handled by the process monitoring the port, or in our case Flask.

A request can either ask for information (GET) or send information (POST). There are variations of requests that imply 
different actions, but we will get by with GET and POST for our project. [Here](https://github.com/rugbyprof/4663-Cryptography/blob/master/Assignments/A08/README.md) is a link to
the project description from Dr. Griffin, which includes an illustration of how this happens.

### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [Program PowerPoint](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A08/client.py)     | Explanation of RSA Public Key Encryption  |
|   2   | [client.py](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A08/client.py)     | Provides a menu to send and receive encrypted messages from server and implements the crypto class  |
|   3   | [crypto_class.py](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A08/client.py)     | Code provided by Dr. Griffin to implement the RSA algorithm  |
|   4   | [key.private.pem](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A08/key.private.pem) | file containing my private key |
|   5   | [key.public.pem](https://github.com/sgilliland/4663-Cryptography-Gilliland/blob/master/Assignments/A08/key.public.pem) | file containing my public key |

### Sources (example)
- I used no outside resources for my program.
