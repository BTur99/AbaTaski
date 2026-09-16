from sys import exit

try:
    e = float(input())

    a = [0, 2]
    k = 2

    while True:
        a.append(2 + 1/a[k - 1])
        
        if abs(a[k] - a[k - 1]) < e:
            print(k, a[k - 1], a[k])
            exit(0)
        
        k += 1
except:
    print("DACKYOU")


