from sys import exit

try:
    a = int(input())
    b = int(input())

    nod = [a, b]
    while nod[0] > 0 and nod[1] > 0:
        if nod[0] > nod[1]:
            nod[0] -= nod[1]
        elif nod[1] > nod[0]:
            nod[1] -= nod[0]
        else:
            nod[0] -= nod[1]


    print(nod[1])


except:
    print("DUCKYOU")
