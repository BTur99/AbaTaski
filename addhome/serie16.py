k = int(input())
l = []

while True:
    a = int(input())
    if a == 0:
        break
    if a > k:
        l.append(a)
print(l[-1])