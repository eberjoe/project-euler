# Largest product of 'n' adjacent factors in a grid
# The 20x20 grid is packed into a csv file

import pandas as pd
from functools import reduce

n = 4
a = []
maxprod = 0

matrix = pd.read_csv('grid.csv', header = None)
for i in range(0, matrix.size):
    a.append(list(map(lambda x: int(x), matrix.iloc[i, 0].split(' '))))

for i in range(0, 20):
    for j in range(0, 20-(n-1)):
        hprod = reduce((lambda x, y: x*y), a[i][j:j+n])
        if i+n <= 20 : d1prod, d2prod = 1, 1
        vprod = 1
        for k in range (0, n):
            vprod *= a[j+k][i]
            if i+n <= 20:
                d1prod *= a[j+k][i+k]
                d2prod *= a[j+k][19-(i+k)]
        maxit = max([hprod, vprod, d1prod, d2prod])
        if maxit > maxprod : maxprod = maxit

print(maxprod)
