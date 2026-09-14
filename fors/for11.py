n = int(input())
sum = 0

if n <= 0:
    exit(1)
    
for i in range(n + 1):
    print(i)
    sum += (n + i)**2

print(f"\n{sum}")