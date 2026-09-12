from sys import exit
from math import pi

pi = round(pi, 2)
a_rad = float(input())

if a_rad < 0 or a_rad > (2 * pi):
    exit(1)

alpha = a_rad * (180 / pi)

print(f"rad = {a_rad} --> grad = {alpha}")