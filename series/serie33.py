from random import randint
try:
    k, n = map(int, input().split())
    m = []
    t = []

    for i in range(k):
        m.append([])
        for j in range(n):
            m[i].append(randint(1, 5))

    for r in range(k):
        lz = 0
        for j in range(n):
            if m[r][j] == 2:
                lz = j + 1
        t.append(lz)

    print(*m) 
    print(*t)
except:
    print("DUCKYOU")