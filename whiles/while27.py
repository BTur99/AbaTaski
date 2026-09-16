try:
    n = 3 # f number here
    f = [0, 1, 1]
    k = 1

    while f[-1] != n:
        f.append(f[k] + f[k + 1])
        k += 1
    print(k + 1) 
    
except:
    print("DUCKYOU")




