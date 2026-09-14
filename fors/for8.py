from sys import exit

a = int(input())
b = int(input())
mult = 1

if a > b:
    exit(1)
    
for i in range(a, b):
    mult *= (i + 1)

print(f"\n{mult}")