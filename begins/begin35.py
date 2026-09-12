from sys import exit

v = int(input())
u = int(input())
if u > v:
    exit(1)
t1 = int(input())
t2 = int(input())

sum_v = v - u
S_lake = v * t1
S_river = sum_v * t2

print(f"S = {S_lake + S_river}")
