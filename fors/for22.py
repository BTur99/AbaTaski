try:
    x = float(input())
    n = int(input())
    r = (1 + x)
    f = 1

    for i in range(2, n + 1):
        f *= i
        r += (x**i)/f
    print(r)
except:
    print("DUCKYOU")