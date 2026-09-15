from sys import exit

a = int(input())
b = int(input())
count = 0

if a <= b:
    exit(1)
    
while b <= a:
    count += 1
    if b <= (a - b):
        a -= b
    else:
        break


print(count)