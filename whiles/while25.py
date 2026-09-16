try:
    n = int(input())
    f = [0, 1, 1]
    k = 1

    while f[-1] < n:
        f.append(f[k] + f[k + 1])
        k += 1
        
    if f[-1] <= n:
        f.append(f[k] + f[k + 1])
        
    print(f[-1]) 
    
except:
    print("DUCKYOU")




