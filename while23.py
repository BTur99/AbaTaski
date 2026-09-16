from sys import exit

try:
    a = int(input())
    b = int(input())

    nod = [a, b]
    print(nod)
    while nod[0] > 0 and nod[1] > 0:
        if nod[0] > nod[1]:
            nod[0] -= nod[1]
            print(1, nod)
        elif nod[1] > nod[0]:
            nod[1] -= nod[0]
            print(2, nod)
        else:
            nod[0]


    print(nod[0])


except:
    print("DUCKYOU")
