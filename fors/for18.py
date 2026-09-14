a = float(input())
n = int(input())

sum = 0

if n <= 0:
    exit(1)
    
for i in range(n + 1):
    if i % 2 == 0:
        sum += a**i

    else:
        sum -= a**i
    
    
print(sum)