try:
    n = int(input())

    a1, a2, a3 = 1, 2, 3
    r = '1 2 3 '

    for i in range(4, n + 1):
        next_a = a3 + a2 - 2*a1
        a1 = a2
        a2 = a3
        a3 = next_a
        r += str(next_a) + ' '

    print(r)
except:
    print("DUCKYOU")