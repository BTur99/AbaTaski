v1 = int(input())
v2 = int(input())
s = int(input())
t = int(input())

sum_v = v1 + v2
sum_s = t * sum_v
final = abs(s - sum_s)

print(f"S start = {s}; {t} t passes\nS final = {final}")