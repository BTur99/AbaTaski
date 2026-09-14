n = int(input())
sum = 1

if n <= 0:
    exit(1)
    
for i in range(n):
    sum *= 1 + ((i + 1) / 10)

print(f"\n{sum}")