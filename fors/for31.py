try:
    n = int(input())

    ak = 2
    r = ''

    for i in range(1, n + 1):
        ak = 2 + 1/ak
        r += str(ak)  +  ' '
        
    print(r)
except:
    print("DUCKYOU")