try:
    k = int(input())

    while True:
        a = int(input())
        if a == 0:
            break
        if a > k:
            print(a)
            break
except:
    print("DUCKYOU")