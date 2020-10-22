## Assignment 7 - Primality Tests
#### Name: Sarah Gilliland
#### Due: Thursday, October 22, 2020



## Certification
### Wilson's Theorem
Wilson's theorem states that a natural number n > 1 is a prime number if and only if (p-1)! ≡ -1 (mod p).
This theorem is a certification of a prime number.

Pseudo code for the algorithm is shown below.

![Pseudocode](/Images/Wilsons.png)

__Sources__
https://primes.utm.edu/notes/proofs/Wilsons.html 
https://en.wikipedia.org/wiki/Primality_test#Fast_deterministic_tests 



## Compositeness

### Solovay-Strassen Test
The Solovay–Strassen primality test is a probabilistic test to determine if a number is composite or probably prime. Therefore, it can be classified as a compositeness test.

The algorithm can be summarized as this: 

We select a number n to test for its primality and a random number a which lies in the range of [2, n-1] and compute its Jacobian (a/n). If n is a prime number, then the Jacobian will be equal to the Legendre and it will satisfy condition (i) given by Euler. If n does not satisfy the given condition then n is composite. For clarification, the Legendre Symbol is defined for a pair of integers a and p such that p is prime. It is denoted by (a/p) and calculated as: 

(a/p) = 0    if a%p = 0
      
(a/p) = 1    if there exists an integer k such that k2 = a(mod p)

(a/p) = -1   otherwise.

The Jacobian of n is a generalization of Legendre Symbol, where p is replaced by n where n is
n = p1k1 * .. * pnkn
, then Jacobian symbol is defined as: 
(a/n) = ((a/p1)^k1) * ((a/p2)^k2) *.....* ((a/pn)^kn)

Using fast algorithms for modular exponentiation, the running time of this algorithm is O(k* log^3 * n), where k is the number of different values of a test.

The pseudocode for calculating the jacobian and for the Solovay-Strassen algorithm is shown below.


![Pseudocode](/Images/SolovayStrassen.png)

__Source__

https://www.geeksforgeeks.org/primality-test-set-4-solovay-strassen/


### Miller-Rabin's Primality Test
Miller-Rabin Primality Test can be considered a Composite test becuase if a number fails this test, it is Composite. If the number passes, it may be a Prime, or it may be a strong pseudoprime. If a number is an odd, positive, composite number, then it passes Miller's test for at most (n-1)/4 bases with 1 <= a <= -1.

Miller showed that any composite number, n, has a Witness less than 70(\ln n)^2 if the Riemann Hypothesis is true.

Pseudo code for the algorithm is shown below.

![Pseudocode](/Images/MillerRabin.png)

__Sources__

https://archive.lib.msu.edu/crcmath/math/math/m/m237.htm

https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/



## Deterministic

### Lucas-Lehmer Test
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


### AKS Primality Test
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

__Sources__

https://www.geeksforgeeks.org/aks-primality-test/?ref=rp 

https://en.wikipedia.org/wiki/AKS_primality_test

