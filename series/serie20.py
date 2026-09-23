try:
    n = int(input())
    l = []
    k = 0
    kh = ''
    for i in range(n):
        l.append(int(input()))
    for j in range(len(l) - 1):
        if l[j] < l[j + 1]:
            k += 1
            kh += str(l[j]) + " "
    print(f"\n{k}\n{kh}")
except:
    print("DUCKYOU")