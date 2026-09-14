n = int(input())

fack = 1
fack_fack = 0

if n <= 0:
    exit(1)
    
for i in range(n):
    fack *= i + 1
    fack_fack += fack

print(fack_fack)