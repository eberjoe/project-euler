a, b, c = 0, 1, 0
while a <= 4000000:
    c = c + (a%2 == 0)*a
    a, b = b, a+b
print(c)
