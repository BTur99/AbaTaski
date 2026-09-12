from math import sqrt

x1, y1 = input().split()
x2, y2 = input().split()

print(sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2))