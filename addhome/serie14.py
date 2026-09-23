k = int(input())
c = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a < k:
        c += 1
print(c)