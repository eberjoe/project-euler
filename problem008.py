# Largest product of 'n' adjacent one-digit factors in a 1000-digit number
# The obnoxious 1000-digit number is packed into a csv file

import pandas as pd
from functools import reduce

n = 13
obnoxious = ''
maxprod = 0

egad = pd.read_csv('obnoxious.csv', header = None)
for i in range(0, egad.size):
    obnoxious += egad.iloc[i, 0]
l = list(filter((lambda x: len(x)), obnoxious.split('0')))
for chunk in l:
    for i in range(0,len(chunk)-(n-1)):
        f = map((lambda x: int(x)), chunk[i:i+n])
        prod = reduce((lambda x, y: x*y), f)
        if prod > maxprod:
            maxprod = prod

print(maxprod)
