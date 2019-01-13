
# First triangular with 'n' divisors

from math import sqrt
from collections import Counter
from functools import reduce

n = 500
s = 0
reach = False

def isPrime(x):
    for i in range(2, int(sqrt(x))+1):
        if x%i == 0: return False
    return True

def orderedPrime(x):
    i = 0
    j = 2
    while i < x:
        if isPrime(j):
            i += 1
            a = j
        j += 1
    return a

def factors(x, skip = False): #factoring with the option to stop if primes skip
    j, k = 1, 0
    f = []
    while x > 1:
        y = orderedPrime(j)
        if x%y == 0:
            k = j
            x /= y
            f.append(y)
        else:
            j += 1
            if skip and k != j-1: break
    return f

def divisorsCount(x):
    exponents = list(Counter(factors(x, True)).values())
    a = list(map(lambda x: x+1, exponents))
    return reduce(lambda x, y: x*y, a)

while not reach:
    s += 4 #select only even numbers from the triangle series
    for i in range(2):
        triangle = sum(range(s+i))
        if divisorsCount(triangle) >= n:
            reach = True
            break

print(triangle)
