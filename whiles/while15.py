from sys import exit

s = 1000
f = 1100
p = float(input())
k = 0

if p <= 0 or p >= 25:
    exit(1)
    
while s < f:
    s += (s * p/100)
    k += 1

if s <= f:
    k += 1
    s += (s * p/100)
    
print(f"month = {k}; sun = {s}")