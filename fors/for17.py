a = float(input())
n = int(input())

sum = 0

if n <= 0:
    exit(1)
    
for i in range(n + 1):
    sum += a**i
    

print(sum)