# Sum of primes below 'n'

from math import sqrt

n = 2000000
a = 0

def isPrime(x):
    for i in range(2, int(sqrt(x))+1):
        if x%i == 0:
            return False
    return True

for j in range(2, n):
    if isPrime(j):
        a += j

print(a)
