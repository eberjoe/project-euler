# Largest palindromic product with factors of 'n' digits

n = 3
floor = 10**(n-1)
ceiling = 10**n
bigpal = 0

for i in range(floor, ceiling):
    for j in range(i, ceiling):
        product = i*j
        if str(product) == str(product)[::-1] and product > bigpal:
            bigpal = product
            f1 = i
            f2 = j
print(f1, "x", f2, "=", bigpal)
