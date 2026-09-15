from sys import exit

n = int(input())
c = 0 
result = 1

if n <= 0:
    exit(1)
    
while (n - c) > 0:
    result *= (n - c)
    c += 2

print(result)