import random
from math import comb

combs = sorted([random.randint(1, 45) for i in range(6)])

print(combs)

print((1 / comb(45, 6)))