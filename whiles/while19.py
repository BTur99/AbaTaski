try:
    n = int(input())
    r = ''

    while n > 0:
        d = n % 10
        n = n // 10
        r += str(d)

    print(r)
except:
    print("DUCKYOU")