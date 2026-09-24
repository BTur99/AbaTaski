def is_act(arr):
    l = arr
    r = False
    c = 0
    for j in range(len(l) - 1):
        if l[j] < l[j + 1]:
            c += 1
    if c == len(l) - 1:
        r = True
    return r

def is_des(arr):
    l = arr
    c = 0
    r = False
    for j in range(len(l) - 1):
        if l[j + 1] < l[j]:
            c += 1
    if c == len(l) - 1:
        r = True
    return r

try:
    k = int(input())
    m = []
    t = []
    for i in range(k):
        m.append([])
        while 0 not in m[i]:
            m[i].append(int(input()))
        m[i].pop()
        if is_act(m[i]):
            t.append(1)
        elif is_des(m[i]):
            t.append(-1)
        else:
            t.append(0)

    print(*m)
    print(*t)
except:
    print("DUCKYOU")