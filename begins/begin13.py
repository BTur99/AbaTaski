from sys import exit
from math import pi

R1 = int(input())
R2 = int(input())
pi = round(pi, 2)


if R1 < R2:
    exit(1)

S1 = pi * R1**2
S2 = pi * R2**2

print(f"S1 = {S1}\nS2 = {S2}\nS3 = {S1 - S2}")