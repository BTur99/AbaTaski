try:
    n = int(input())
    f1, f2 = 1, 1
    r = "1 1 "
    for i in range(3, n + 1):
        next_f = (f1 + f2)
        f1 = f2
        f2 = next_f
        r += str(next_f) + " "
        
    print(r)
except:
    print("DUCKYOU")