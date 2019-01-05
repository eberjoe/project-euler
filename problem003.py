#Largest prime factor of 'n'

import math

n = 600851475143
maxi = "no prime factors"

def isPrime(x):
    a = int(math.sqrt(x))
    for i in range(2, a+1):
        if x%i == 0:
            return False
    return True

for i in range(2, int(math.sqrt(n))+1):
    if isPrime(i):
        if n%i == 0:
            maxi = i

print(maxi)
