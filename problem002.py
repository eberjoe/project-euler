# Sum of even Fibonacci numbers equal or less than 'n'

a, b, c, n = 0, 1, 0, 4000000

while a <= n:
    c = c + (a%2 == 0)*a
    a, b = b, a+b

print(c)
