# Longest Collatz series with a start number under 'n'

n = 1000000
longest = []

def Collatz(x):
    s = [x]
    while x > 1:
        if x%2 == 0:
            x /= 2
        else:
            x = 3*x+1
        s.append(x)
    return list(map(lambda x: int(x), s))

for i in range(n, 13, -1):
    if len(Collatz(i)) > len(longest): longest = Collatz(i)

print(longest[0])
