from sys import exit
try:
    n = int(input())

    while n > 0:
        if (n % 10) % 2 != 0:
            print(True)
            exit(0)
        n = n // 10

    print(False)
except:
    print("DUCKYOU")