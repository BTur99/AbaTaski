try:
    n = int(input())
    l = []
    z = []
    for i in range(n):
        l.append(int(input()))

    for j in range(len(l)):
        if l[j] == 0:
            z.append(j)

    s = sum(l[z[-2]: z[-1]])

    print(f"\n{s}")
except:
    print("DUCKYOU")