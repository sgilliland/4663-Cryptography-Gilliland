## Assignment 7 - Primality Tests
#### Name: Sarah Gilliland
#### Due: Tuesday, October 20, 2020

### Certification
#### Certification test ...
__Sources__

### Compositeness
#### Compositeness Test ...
__Sources__


### Deterministic
#### Lucas-Lehmer Test
The Lucas-Lehmer Test is a deterministic algorithm and is the primality test used by the
[Great Internet Mersenne Prime Search](https://en.wikipedia.org/wiki/Great_Internet_Mersenne_Prime_Search) (GIMPS) to locate large primes. 
This search has been successful in locating many of the largest primes known to date.
In 1878, E. Lucas proposed two tests for the primality of the Mersenne number, N = 2n − 1. 
However, neither was accompanied by a complete proof. In 1930, and as part of his Ph.D. thesis, 
D. H. Lehmer stated and proved a necessary and sufficient condition for N to be prime. 
This result has become known as the Lucas–Lehmer test. It is usually stated as in Theorem 1.

![Theorem](/Images/2020-10-20.png)

The pseudocode of the Lucas-Lehmer Test is shown below.

![Pseudocode](/Images/PseudoCodeLLT.png)

__Sources__

https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test 

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.107.3573&rep=rep1&type=pdf 


#### AKS Primality Test
The AKS (Agrawal–Kayal–Saxena) Primality Test is a deterministic algorithm that can be used to verify the primality of any general number given. 
The AKS Primality Test was created and published by Manindra Agrawal, Neeraj Kayal, and Nitin Saxena in 2002.
The AKS primality test is based upon the following theorem: An integer n greater than 2 is prime if and only if the polynomial congruence relation 

![TheoremPt1](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-2a71ba1e4c187329dbf2eb5ed2baf765_l3.svg) 

holds for some a coprime to n. Here x is just a formal symbol. 
The AKS test evaluates the equality by making complexity dependent on the size of r . This is expressed as

![TheoremPt2](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-8073198e20b3072fcccea50221cd428a_l3.svg) 

which can be expressed in simpler terms as 

![TheoremPt3](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-80cb6414a1344ccdce4e4b37042dfbe8_l3.svg) 

for some polynomials f and g.
This congruence can be checked in polynomial time when r is polynomial to the digits of n.

Here is some python3 code to check if a number, n, is prime. This program demonstrates concept behind AKS algorithm and doesn't implement the actual algorithm.
(This works only till n = 64) 
![CPPCode](/Images/AKSpython.png)
