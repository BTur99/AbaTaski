try:
    k, n = map(int, input().split())
    r = ''

    for i in range(n):
        r += str(float(input())**k) + ' '
    print(r)
except:
    print("DUCKYOU")