# Sum of the letters of all written out numbers from 1 to 'n' (under 1010)

from math import log10

n = 1000
d = 0

units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
X = ['', 'hundred', 'thousand', '']

for i in range(1, n+1):
    k = str(i)
    b = int(i/10)%10
    if b == 1 and k[-1] != '0':
        a = len(teens[i%10])
        b = 0
    else:
        a = len(units[i%10])
    c = int(log10(i))-1
    d += a + len(tens[b]) + len(X[c]) + (c>0)*len(units[int(i/10**(c+1))]) + (len(str(i))>2 and k[-2:]!='00')*3

print(d)
