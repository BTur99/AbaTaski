from random import randint
try:
    k, n = map(int, input().split())
    m = []
    t = []

    for i in range(k):
        m.append([])
        for j in range(n):
            m[i].append(randint(1, 10))

    for k in range(len(m)):
        for p in range(n):
            if 2 not in m[k]:
                t.append(0)
                break
            else:
                if m[k][p] == 2:
                    t.append(p)
                    break

    print(*m)
    print(*t)
except:
    print("DUCKYOU")