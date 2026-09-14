n = int(input())
sum = 0

if n <= 0:
    exit(1)
    
for i in range(1, n * 2):
    if i % 2 != 0:
        sum += i
        print(sum)
