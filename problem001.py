# Sum of multiples of 3 and 5 less than 'n'

j, n = 0, 1000
for i in range (3, n):
    j += i * ((i%3 * i%5) == 0)

print(j)
