from sys import exit

a = int(input())
b = int(input())
sum = 0

if a >= b:
    exit(1)
    
for i in range(a, b + 1):
    sum += i

print(f"\n{sum}")