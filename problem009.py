# Pythagorean triple: a+b+c=n when a<b<c and c**2 = a**2 + b**2

n = 1000
answer = 'No triple here :('

for i in range(int(n/3)+1, n-2):
    for j in range(int((n-i)/2)+1, n-i):
        if i**2 == j**2 + (n-i-j)**2:
            answer = 'a = ' + str(n-j-i)+'; b = '+str(j)+'; c = '+str(i)+': a + b + c = '+str(n)+'; a * b * c = '+str((n-i-j)*j*i)
            break

print(answer)
