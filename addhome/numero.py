from random import randint

numero = randint(1, 100)
count = 0

while True:
    n = int(input())
    if n < numero:
        print("Число больше")\
        count += 1
    elif n > numero:
        print("число меньше")
        count += 1
    else:
        print(f"Ты угадал заданое число {numero}")
