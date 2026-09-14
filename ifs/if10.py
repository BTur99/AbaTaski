from sys import exit

n = int(input())
sum = 0

if n < 0:
    exit(1)

for i in range(n):
    sum += (1 / (i + 1))
    print(f"1/{i + 1}")
print(sum)