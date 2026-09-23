n = int(input())
s = 0
m = 1
for i in range(n):
    a = float(input())
    s += a
    m *= a
print(s, m)