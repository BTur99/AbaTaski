from sys import exit

a = int(input())
b = int(input())

print("\n")
if a >= b:
    exit(1)

for i in range(a + 1, b):
    print(b - 1)
    b -= 1
