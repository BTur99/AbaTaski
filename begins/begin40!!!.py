a1, b1, c1, a2, b2, c2  = map(int, input().split())

D = a1 * b2 - a2 * b1
x = (c1 * b2 - c2 * b1) / D
y = (a1 * c2 - a2 * c1) / D

print(f"({x}; {y})")