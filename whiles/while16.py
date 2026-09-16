from sys import exit
try:
    s = 10 
    p = float(input())
    k = 1

    if p <= 0 or p >= 50:
        exit(1)

    while s <= 200:
        print(k, s)
        k += 1
        s += (p/100 * s)

    if s <= 200:
        k += 1
        s += (p/100 * s)

    print(k, s)
except:
    print("DUCKYOU")