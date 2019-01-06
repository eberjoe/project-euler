# Smallest number divisible by all integers from 1 through 'n'

n = 20
a = n
b = 0

while b < n:
    a += n
    for i in range(1, n+1):
        if a%i != 0:
            break
        b = i
print(a)
