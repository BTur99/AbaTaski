try:
    a, b = map(int, input().split())

    for i in range(a, b + 1):
        r = i - a + 1
        print(str(i) * r)
except:
    print("DUCKYOU")