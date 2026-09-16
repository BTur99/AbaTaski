from sys import exit

try:
    n = int(input())
    f = [0, 1, 1]
    k = 1

    while f[-1] < n:
        f.append(f[k] + f[k + 1])
        if n in f:
            print(True)
            exit(0)
        k += 1
    print(False)
    
except:
    print("DUCKYOU")
    




