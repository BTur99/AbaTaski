try:
    n = int(input())

    a1, a2 = 1, 2
    r = '1 2 '

    for i in range(3, n + 1):
        next_a = (a1 + 2*a2)/3
        a1 = a2
        a2 = next_a
        r += str(next_a) + ' '

    print(r)
except:
    print("DUCKYOU")