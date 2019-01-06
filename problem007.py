# Find the nth prime

import math

n = 10001
k = 0
i = 1

def isPrime(x):
    a = int(math.sqrt(x))
    for i in range(2, a+1):
        if x%i == 0:
            return False
    return True

while k < n:
    i += 1
    k += isPrime(i)

print(i)
