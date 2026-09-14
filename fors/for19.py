n = int(input())

fack = 1

if n <= 0:
    exit(1)
    
for i in range(n):
    fack *= i + 1


print(fack)