n = int(input())
sum = 0

if n <= 0:
    exit(1)
    
for i in range(n):
    if i % 2 != 0:
        sum += 1 + ((i + 1) / 10)

    else:
        sum -= 1 + ((i + 1) / 10)


print(f"\n{sum}")