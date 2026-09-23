try:
    k = int(input())
    m = []
    c = []
    for i in range(k):
        m.append([])
        cn = 0
        while 0 not in m[i]:
            m[i].append(int(input()))
            cn += 1
        c.append(cn - 1)
        m[i].pop()

    print(*m)
    print(*c)
except:
    print("DUCKYOU")