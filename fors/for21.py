try:
    n = int(input())
    f = 1
    r = 1

    for i in range(n):
        f *= (i + 1)    
        r += 1/f
    print(r)
except:
    print("DUCKYOU")