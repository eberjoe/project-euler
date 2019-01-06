# Sum of the squares, minus the square of the sum of the first 'n' natural numbers

n = 100
a, b = 0, 0
for i in range(1, n+1):
    a += i
    b += i**2
    
print(a**2-b)
