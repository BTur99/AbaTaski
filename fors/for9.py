from sys import exit

a = int(input())
b = int(input())
sqr = 1

if a > b:
    exit(1)
    
for i in range(a, b):
    sqr += (i + 1)**2

print(f"\n{sqr}")