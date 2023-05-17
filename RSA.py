# Generate a public and private key
# Show the process of encryption
# Show the decryption

#Choose two large prime numbers p and q

#Choose a random number

#Check if the number is prime
#if not repeat until random number is prime
#Repeat process twice to find p and q

#Calculate the product n=pq

#Find lambda(n)

#Choose an integer e such that 2 < e < lambda(n). e and lambda(n) are coprime

#Find d=e^-1(mod(lambda(n))) 

import secrets
from math import sqrt, floor

def randPrime(bits: int):
    prime = False
    while prime == False:
        randNum = secrets.randbits(bits)
        if randNum > 2:
            prime = isPrime(randNum)
    return randNum

def isPrime(num: int):
    for x in range(2, floor(sqrt(num)) + 1):
        if (num%x) == 0:
            return False
    return True




