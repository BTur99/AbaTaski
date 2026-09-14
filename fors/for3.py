from sys import exit

a = int(input())
b = int(input())

if a >= b:
    exit(1)
    
for i in range(b, a - 1, -1):
    print(i)