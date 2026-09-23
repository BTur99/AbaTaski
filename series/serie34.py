from random import randint
try:
    k, n = map(int, input().split())
    m = []
    s = []

    for i in range(k):
        m.append([])
        for j in range(n):
            m[i].append(randint(1, 10))

    for r in range(k):
        if 2 in m[r]:
            s.append(sum(m[r]))  # Если есть 2, добавляем сумму
        else:
            s.append(0)   

    print(*m)
    print(*s)
except:
    print("DUCKYOU")