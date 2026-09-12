from sys import exit
from math import sqrt

a = int(input())
b = int(input())
c = int(input())
if a == 0 or (a > 0 and b > 0 and c > 0):
    exit(1)

D = b**2 - 4 * a * c
x1 = (-b + sqrt(D)) / (2 * a)
x2 = (-b - sqrt(D)) / (2 * a)

print(f"x1 = {x1}\nx2 = {x2}")