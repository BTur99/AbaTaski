from random import randint

s, f = map(int, input("Введи два числа через пробел(диапозон числе): ").split())
numero = randint(s, f)
count = 0
best_result = 0

while 2**best_result < numero:
    best_result += 1

while True:
    n = int(input("Введи число: "))
    if n < numero:
        print("Число больше")
        count += 1
    elif n > numero:
        print("число меньше")
        count += 1
    else:
        if count > best_result:
            print(f"Да ты угадал {numero}, но потратил {count} попыток, а надо уложиться в {best_result} попыток")
            break
        else:
            print(f"Ты угадал заданое число {numero}\nТы портратил {count} попыток")
            break

