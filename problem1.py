j = 0
for i in range (3,1000):
    j = j + i * ((i%3 * i%5) == 0)
print(j)
