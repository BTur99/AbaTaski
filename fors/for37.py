try:
    n = int(input())
    s = 0

    for i in range(1, n + 1):
        s += float(i**n)
    print(s)
except:
    print("DUCKYOU")