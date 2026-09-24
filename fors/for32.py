try:
    n = int(input())

    ak = 1
    r = ''

    for i in range(1, n + 1):
        ak = (ak + 1)/i
        r += str(ak)  +  ' '
        
    print(r)
except:
    print("DUCKYOU")