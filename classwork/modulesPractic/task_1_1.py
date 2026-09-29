import sys

print("Python version:", sys.version.split()[0])
print("Executable:", sys.executable)

print("Path count:", len(sys.path))
for p in sys.path[:4]:
    print("    ", p)

import math, random

print("pi =", math.pi)
print("random() =", random.random())

mods = sorted(sys.modules)
print("Module count:", len(mods))

public = [n for n in dir(math) if not n.startswith('__')]
print("Public count:", len(public))
print("First 8:", public[:8])

print("Иой __name__ =", __name__)
print("Иой __file__ =", __file__)

'''
Вопросы для самопроверки + повыш слжности

1.  Для удобства, чтобы имрпортировать модули рядом со скриптом. 
    Если назвать свой модуль также как стандартный питон обратиться именно
    к нашему файлу и это вызовет Атрибут ерор
2.  Прямо вызвать функцию через фром быстрее чем искать фукц по всему модулю.
    Фром подгружает функции и тд по отдельности, а обычным импортом весь модуль
3.  Питон обратиться к нашему файлу первее и будет там искать функц, не найдет и кинет Атр Ерор

'''
