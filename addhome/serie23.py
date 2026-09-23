n = int(input())
p = []


for i in range(n):
    p.append(float(input()))

for j in range(len(p) - 1):
    if (p[j] < p[j + 1] and p[j] < p[j - 1]) or (p[j] > p[j + 1] and p[j] > p[j - 1]):
        c += 1