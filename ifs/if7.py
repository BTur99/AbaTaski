from sys import exit

a, b = map(int, (input()).split())

sum = 0 

if a >= b:
    exit(1)

for i in range(a, b + 1):
    sum += i
print(sum)

