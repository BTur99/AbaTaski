try:
    x = float(input())
    n = int(input())

    r = x
    t = x
    for i in range(1, n + 1):
        t *= -x * x * ((2 * i - 1) / (2 * i + 1))
        r += t
    print(r)
except:
    print("DUCKYOU")