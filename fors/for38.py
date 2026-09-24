try:
    n = int(input())
    s = 0
    b = n
    for i in range(1, n + 1):
        s += float(i**b)
        b -= 1
    print(s)
except:
    print("DUCKYOU")