try:
    n = int(input())
    c = 0
    s = 0

    while n > 0:
        d = n % 10
        n = n // 10
        c += 1
        s += d
    print(c, s)
except:
    print("DUCKYOU")