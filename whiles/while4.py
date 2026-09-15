from sys import exit

n = int(input())
c = 1

if n <= 0:
    exit(1)
    
while n >= 3**c:
    if n == 3**c:
        print(True)
        exit(0)
    c += 1
print(False)
    