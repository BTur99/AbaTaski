from sys import exit
try:
    n = int(input())
    k = 2

    while k < 10:
        if n % k == 0 and k != n and k != 1:
            print(False)
            exit(0)
        k += 1

    print(True)
except:
    print("DUCKYOU")