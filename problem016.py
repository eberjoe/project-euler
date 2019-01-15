# Sum of the digits of 2 raised to the nth power

n = 1000

print(sum(list(map(lambda x: int(x), str(2**n)))))
