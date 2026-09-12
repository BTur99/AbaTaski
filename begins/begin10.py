from sys import exit

a = int(input())
b = int(input())

if a == 0 or b == 0:
    exit(1)

print(f"sum = {a + b}\nsub = {a - b}\nmult = {a * b}\ndiv = {a / b}")