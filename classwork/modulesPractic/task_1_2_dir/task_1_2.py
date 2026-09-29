import mymodule
from mymodule import circle_area
from mymodule import circle_len as perimeter
import mymodule as mm

'''
help(mymodule)

FUNCTIONS
    circle_area(r)

    circle_len(r)

    sphere_volume(r)
        Возвращает объем сферы радиуса r.
'''

print(dir(mymodule))
print(mymodule.__name__)
print(mymodule.__file__)
print(mymodule.circle_area(5))
print(circle_area(5))
print(perimeter(5))
print(mm.PI)

print(mm._helper())

'''
Вопросы для самопроверки + повыш слжности

1.  нэйм мэин нужен для того чтобы невыполнять все коды, а все коды только
    если запускать сам файлик

2.  фром модуль звезда плохо, т.к могут возникнуть конфликты если имена были
    переназначены

3.  mymodule / __main__ т к именно этот скрипт мы запускаем
'''
