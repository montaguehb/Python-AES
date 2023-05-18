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

#Find d=e^-1(modulo(lambda(n))) 

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

def ctz(num: int):
    return (num & -num).bit_length()-1

def gcd(a: int, b: int):
    if a == 0:
        return a
    if b == 0:
        return b
    shift = (ctz(a), ctz(b))[ctz(a) > ctz(b)]
    a >>= ctz(a)
    while b != 0:
        b >>= ctz(b)
        b -= a
        c = b >> 31
        a += b & c
        b = (b + c) ^ c
    return a << shift

def lcm(a: int, b: int):
    return int((a * b)/gcd(a, b))

def findE(a: int):
    e = randPrime(8)
    while (e > a | e < 2) & (gcd(e, a) > 1):
        e = randPrime(8)
    return e

p = randPrime(8)
q = randPrime(8)
n = p * q

print(p, q, n)
lambdaN = lcm(p - 1, q - 1)
e = findE(lambdaN)
d = pow(e, -1, lambdaN)

# c = pow(1000, e, n)
# print(p, q, n)
# print(pow(c, d, n))


