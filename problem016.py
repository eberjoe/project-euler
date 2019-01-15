# Sum of the digits of the nth power of 2

n = 1000

print(sum(list(map(lambda x: int(x), str(2**n)))))
