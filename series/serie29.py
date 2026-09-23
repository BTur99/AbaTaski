from random import randint
try:
    k, n = map(int, input().split())
    m = []
    s = 0

    for i in range(k):
        m.append([])
        for j in range(n):
            m[i].append(randint(1, 10))

    for k in m:
        for p in k:
            s += p

    print(*m)
    print(*s)
except:
    print("DUCKYOU")