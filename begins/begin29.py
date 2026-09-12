from sys import exit
from math import pi

pi = round(pi, 2)
alpha = int(input())

if alpha < 0 or alpha > 360:
    exit(1)

a_rad = alpha * (pi / 180)

print(f"grad = {alpha} --> rad = {a_rad}")