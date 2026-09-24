try:
    from math import sin

    n = int(input())
    a, b = map(float, input().split())

    h = (b - a)/n
    r = ''
    for i in range(n + 1):
        x = a + h * i
        fx = 1 - sin(x)
        r += f"f({x}) = {fx}\n"
    print(r)
except:
    print("DUCKYOU")