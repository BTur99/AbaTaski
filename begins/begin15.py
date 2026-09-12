from math import pi, sqrt

pi = round(pi, 2)
S = int(input())

D = round(sqrt(pi * 4 * S), 2)
L = round(pi * D, 2)

print(f"D = {D}\nL = {L}")