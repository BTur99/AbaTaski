try:
    x = float(input())
    n = int(input())

    r = 1
    t = 1

    for i in range(1, n + 1):
        t *= -(2 * i - 3) * x / (2 * i)
        r += t
    print(r)
except:
    print("DUCKYOU")