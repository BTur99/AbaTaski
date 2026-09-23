try:
    n = int(input())
    l = []
    c = 0
    for i in range(n):
        l.append(int(input()))
    for j in range(len(l) - 1):
        if l[j + 1] < l[j]:
            c += 1
        else:
            print(f"\n{l[j + 1]}")
            break
    if c == len(l) - 1:
        print(0)
except:
    print("DUCKYOU")