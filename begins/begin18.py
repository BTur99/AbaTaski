from math import sqrt

xa, ya = input().split()
xb, yb = input().split()
xc, yc = input().split()

if (xb < xc < xa) or (xa < xc < xb):
    AC = sqrt((int(xc) - int(xa))**2 + (int(yc) - int(ya))**2)
    BC = sqrt((int(xc) - int(xb))**2 + (int(yc) - int(yb))**2)

    print(f"AB = {AC}\nBC = {BC}\nAC = {AC + BC}")