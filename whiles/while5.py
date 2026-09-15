from sys import exit
from random import randint

n = 2**(randint(1, 10))
c = 1

if n <= 0:
    exit(1)
    
while n >= 2**c:
    if n == 2**c:
        print(f"{n} = 2**{c}")
        exit(0)
    c += 1
    