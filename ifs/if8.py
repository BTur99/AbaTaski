from sys import exit

a = int(input())
b = int(input())

if a >= b:
    exit(1)

for i in range(a, b + 1):
    for j in range(a, b + 1):
        print(f"{i} * {(j)} = {i * j}")
    print("\n")
