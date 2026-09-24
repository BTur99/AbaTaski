try:
    n = int(input())
    p = []
    c = 0

    for i in range(n):
        p.append(float(input()))

    for j in range(1, len(p) - 1):
        if (p[j] < p[j + 1] and p[j] < p[j - 1]) or (p[j] > p[j + 1] and p[j] > p[j - 1]):
            c += 1
        else:
            if j != 0 and j != len(p):
                print(f"\n{p[j + 1]}")
                break
            
    if c == len(p) - 2:
        print(0)
except:
    print("DUCKYOU")