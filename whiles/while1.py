from sys import exit

a = int(input())
b = int(input())

if a <= b:
    exit(1)
    
while b <= a:
    if b <= (a - b):
        a -= b
    else:
        break


print(a - b)