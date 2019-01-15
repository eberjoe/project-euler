# Lattice paths for an 'n'x'n' grid

n = 20

def factorial(x):
    for i in range(1, x):
        x *= i
    return x

def binomialCoef(x, y):
    return int(factorial(x)/(factorial(y)*factorial(x-y)))

print(binomialCoef(n*2, n))
