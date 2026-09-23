try:
    n = int(input())
    l = []
    r = False
    c = 0
    for i in range(n):
        l.append(int(input()))
    for j in range(len(l) - 1):
        if l[j] < l[j + 1]:
            c += 1

    if c == len(l) - 1:
        r = True
    print(r)
except:
    print("DUCKYOU")