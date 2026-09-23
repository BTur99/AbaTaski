from random import randint

k, n = map(int, input().split())
m = []
c = 0

for i in range(k):
    m.append([])
    for j in range(n):
        m[i].append(randint(1, 10))

for k in m:
    if 2 in k:
        c += 1

print(*m)
print(c)