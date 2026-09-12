from math import sqrt

xa, ya = input().split()
xd, yd = input().split()

xb, yb = xd, ya

'''
a           b

c           d
'''

AB = sqrt((int(xb) - int(xa))**2 + (int(yb) - int(ya))**2)
BD = sqrt((int(xd) - int(xb))**2 + (int(yd) - int(yb))**2)

print(f"S = {AB * BD}\nP = {2 * (AB + BD)}")