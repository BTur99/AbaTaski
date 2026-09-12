from math import sqrt

x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()

a = sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)
b = sqrt((int(x3) - int(x2))**2 + (int(y3) - int(y2))**2)
c = sqrt((int(x3) - int(x1))**2 + (int(y3) - int(y1))**2)

p = (a + b + c) / 2
S = sqrt(p * (p - a) * (p - b) * (p - c))
print(f"S = {S}")