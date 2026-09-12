from math import pi

pi = round(pi, 2)
L = int(input())

R = round(L / (2 * pi), 2)
S = round(pi * R**2, 2)

print(f"R = {R}\nS = {S}")