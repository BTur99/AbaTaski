import random

N = 100000
c = {}

for i in range(N):
    s = 0
    for j in range(3):
        s += random.randint(1, 6)
    if str(s) not in c.keys():
        c[str(s)] = 1
    else:
        c[str(s)] += 1

for k, v in c.items():
    if v == max(c.values()):
        print(f"{k}: {v}")