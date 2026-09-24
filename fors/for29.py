try:
    n = int(input())
    a, b = map(float, input().split())

    h = (b - a)/n
    r = ''

    for i in range(n + 1):
        r += str(a + h * i) + ' '

    print(r)
except:
    print("DUCKYOU")