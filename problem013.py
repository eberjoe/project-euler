# First 'n' digits of the sum of 100 50-digit numbers taken from a csv file

import pandas as pd

n = 10
c = []

s = pd.read_csv('100x50sum.csv', header = None)
for i in range(s.size):
    c.append(int(s.iloc[i, 0]))

print(str(sum(c))[:n])
